import random, posixpath, hashlib
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class RandomNameStorage(FileSystemStorage):
    def get_valid_name(self, name):
        file_root, file_ext = posixpath.splitext(name)
        chars,ret = u'abcdefghijklmnopqrstuvwxyz1234567890', u''
        for i in range(16):
            ret += random.choice(chars)
        sha1 = hashlib.sha1(file_root)
        sha1.update(ret)
        return sha1.hexdigest() + file_ext

