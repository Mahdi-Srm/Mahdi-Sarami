from main import karnameh

def save_to_file(data, filename='result.txt'):
    try:
        with open(filename, 'a') as file:
            file.write("Student Information:\n")
            for key, value in data.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
        print("Data successfully saved to", filename)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    student_data = karnameh()
    if student_data:
        save_to_file(student_data)
