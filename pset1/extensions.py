extension_dict = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
    }

common_default = 'application/octet-stream'

extension = input("Please enter File Name: ").rpartition('.')[-1].lower().strip()

print(extension_dict.get(extension, common_default))

