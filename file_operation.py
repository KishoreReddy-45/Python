#file operation

def update_server_config(file_path, key, value):
  # create a file
  with open(file_path, "r") as file:
    lines = file.readlines()

  # create a file in update mode
  with open(file_path, "w") as file:
    for line in lines:
        if key in line:
          file.write(key + "=" + value + "\n")
        else:
          file.write(line)
      
update_server_config("server.config","MAX_CONNECTIONS","100")
