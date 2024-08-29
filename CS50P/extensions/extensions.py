string = (input("File Name: ").strip(" ")).lower()

i = 0
sub_string = ""

while i < len(string):
    if string[i] == ".":
        sub_string = string[(i + 1):]
    i += 1

if sub_string == "jpeg" or sub_string == "jpg":
    print("image/jpeg")
elif sub_string == "pdf" or sub_string == "zip":
    print(f"application/{sub_string}")
elif sub_string == "gif" or sub_string == "png":
    print(f"image/{sub_string}")
elif sub_string == "txt":
    print("text/plain")
else:
    print("application/octet-stream")


