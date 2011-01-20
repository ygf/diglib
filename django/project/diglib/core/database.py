# -*- coding: utf-8 -*-


class Database(object):
    
    # Add a document to the database and return a subclass of the Document
    # class representing the document in the database.
    def add(self, hash_md5, hash_ssdeep, mime_type, document_path,
            document_size, thumbnail_path, language_code, tags):
        raise NotImplementedError()

    def update_tags(self, hash_md5, tags):
        raise NotImplementedError()
    
    def get(self, hash_md5):
        raise NotImplementedError()    

    def delete(self, hash_md5):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()