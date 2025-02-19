import os
from feedback import Feedback


class AudioFile:
    def __init__(self, org_name: str, location: str, title: str, artist: str):
        self.org_name: str = org_name.strip()
        self.location: str = location
        self.title: str = title.rstrip()
        self.artist_name: str = artist.rstrip()
        self.year: str = None
        self.file_format: str = None
        self.new_name: str = None
        self.feedback = Feedback()
        self.org_exists = os.path.exists(os.path.join(self.location))
        self._new_exists = False
        self.determine_format()

    def __str__(self):
        return self.artist_name + ' - ' + self.title + '.' + self.file_format

    def determine_format(self):
        if self.org_name is not None:
            fname = self.org_name.split(".")
            self.file_format = fname[-1]

    def rename(self):
        if self.new_name is None:
            self.new_name = self.artist_name + ' - ' + self.title + '.' + self.file_format
            self.feedback.log('New filename not provided. Cannot rename!')

        if self.location is None:
            self.location = os.getcwd()

        if not os.path.exists(self.location):
            self.feedback.error("WARNING: Location does not exist!")
            return False

        old_name = os.path.join(self.location, self.org_name)
        new_name = os.path.join(self.location, self.new_name)

        if not self.org_exists:
            self.feedback.error("WARNING: Original file does not exist!")
            return False

        try:
            self.feedback.log(f"Rename {old_name} to {new_name}")
            os.rename(old_name, new_name)
            self._new_exists = os.path.exists(old_name)
        except FileExistsError:
            self.feedback.error('New File already exists')
            return False
        except OSError:
            self.feedback.error('File does not exist')
            return False

        return self._new_exists
