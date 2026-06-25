from rag import rag_pipeline

import questions_generator

def main():

    print("Welcome to the DSA Solution")

    while True:

        print("\n")
        print("1. Solve Question")
        print("2. Generate Question")
        print("3. Exit")

        choice = input("Select Option: ")

        if choice == '1':

            query = input("Enter the question (type 'exit' to quit): ")
            language = input("Select the language: ")

            if query.lower() == 'exit':

                break

            response = rag_pipeline(query, language)

            print(response)

        elif choice == '2':

            topic = input("Enter the topic: ")
            difficulty = input("Enter the difficulty: ")
            language = input("Select the language: ")

            response = questions_generator.generate_question(topic, difficulty, language)

            print(response)

        elif choice == '3':

            break


if __name__ == "__main__":
    main()