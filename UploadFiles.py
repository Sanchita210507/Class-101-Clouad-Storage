import dropbox 

class Transferdata:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')

        dbx.files_upload(f.read(),file_to)

def main():
    access_token='s5RWdRPJtp8AAAAAAAAAAXG3l9Sarb6EGdVPBZ0kHlMme_mMsh_wXBYkANwSwkd0'
    td=Transferdata(access_token)

    file_from=input("Enter the file path: ")
    file_to= input("Enter the file path to upload to dropbox: ")

    td.upload_file(file_from,file_to)
    print("Files have been moved!")

main()