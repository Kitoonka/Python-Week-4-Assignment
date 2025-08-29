def read_and_modify():
    filename = input("Enter the filename to read: ")
    try:
        # Open and read the original file
        with open(filename, "r") as file:
            content = file.read()

        # 🔹 Modify content (example: uppercase + line numbers)
        lines = content.splitlines()
        modified_content = "\n".join(f"{i+1}: {line.upper()}" for i, line in enumerate(lines))

        # 🔹 Save into new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ Modified content saved in '{new_filename}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the function
read_and_modify()
