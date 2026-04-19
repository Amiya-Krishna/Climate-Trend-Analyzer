def chatbot(df):
    print("\n🤖 Climate Chatbot Ready (type 'exit' to stop)")

    while True:
        q = input("Ask question: ")

        if q.lower() == "exit":
            break

        if "max" in q.lower():
            print(df["Temperature"].max())

        elif "min" in q.lower():
            print(df["Temperature"].min())

        elif "average" in q.lower():
            print(df["Temperature"].mean())

        else:
            print("Try: max, min, average")