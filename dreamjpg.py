import io, os, sys, shutil

def delete_bytes(file_path, start_byte, end_byte):
    shutil.copy(file_path, file_path+".tmp")
    file_path_tmp = file_path+".tmp"
    with io.open(file_path_tmp, "rb") as f:
        file_data = f.read()

    # Delete the bytes from the file data.
    file_data = file_data[:start_byte] + file_data[end_byte:]

    # Write the updated file data to the file.
    with io.open(file_path_tmp, "wb") as f:
        f.write(file_data)

    f.close()
    shutil.copy(file_path_tmp, file_path+'.jpg')
    os.remove(file_path_tmp)


if __name__ == "__main__":
    if sys.argv[1]:
        file_path = sys.argv[1]
        start_byte = int(0x0000)
        end_byte = int(0x1480)

        delete_bytes(file_path, start_byte, end_byte)
