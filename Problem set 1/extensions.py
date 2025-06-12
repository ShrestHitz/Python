file_name = input("Enter the file name: ").strip()

# Convert the file name to lowercase for case-insensitive comparison
file_name_lower = file_name.lower()

if file_name_lower.endswith(".jpg") or file_name_lower.endswith(".jpeg"):
    print("image/jpeg")
elif file_name_lower.endswith(".png"):
    print("image/png")
elif file_name_lower.endswith(".gif"):
    print("image/gif")
elif file_name_lower.endswith(".pdf"):
    print("application/pdf")
elif file_name_lower.endswith(".txt"):
    print("text/plain")
elif file_name_lower.endswith(".zip"):
    print("application/zip")
elif file_name_lower.endswith(".mp4"):
    print("video/mp4")
elif file_name_lower.endswith(".mp3"):
    print("audio/mpeg")
else:
    print("application/octet-stream")