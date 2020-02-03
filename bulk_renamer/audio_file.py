import os
from feedback import Feedback


class AudioFile:
    def __init__(self, org_name: str, location: str, title: str, artist: str):
        self.org_name: str = org_name
        self.location: str = location
        self.title: str = title
        self.artist_name: str = artist
        self.year: str = None
        self.file_format: str = None
        self.new_name: str = None
        self.feedback = Feedback()
        self.exsits = False
        self.determine_format()

    def determine_format(self):
        fname = self.file_format.split(".")
        self.file_format = fname[-1].lower()

    def rename(self):
        if self.new_name is None:
            self.new_name = self.artist_name + ' - ' + self.title
            self.feedback.log('New filename not provided. Cannot rename')

        if self.location is None:
            self.location = os.getcwd()

        if not os.path.exists(self.location):
            self.feedback.error("WARNING: Location does not exist!")
            return False

        old_name = os.path.join(self.location, self.org_name)
        new_name = os.path.join(self.location, self.new_name)

        if not os.path.exists(old_name):
            self.feedback.error("WARNING: Original file does not exist")
            return False

        try:
            os.rename(old_name, new_name)
        except FileExistsError:
            self.feedback.error('New File already exists')
            return False
        except OSError:
            self.feedback.error('File does not exist')
            return False

        return True
