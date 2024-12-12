import ollama_client

def main():
  # Using LLaVA for image analysis
  with open('image.jpg', 'rb') as file:
    response = ollama_client.client().chat(
      model='llava:13b',
      messages=[
        {
          'role': 'user',
          'content': 'Copy the texts from the image.',
          'images': [file.read()],
        },
      ],
    )

  print(response['message']['content'])


if __name__ == '__main__':
  main()