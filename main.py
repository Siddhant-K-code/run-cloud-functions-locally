import functions_framework

@functions_framework.http
def main(request):
    return f'Hello, {request.json.get("name")}\n'

if __name__ == "__main__":
    main()
