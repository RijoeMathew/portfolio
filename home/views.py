from django.shortcuts import render
import openai
from django.conf import settings

def homepage(request):
    if request.method == 'POST':
        
        openai.api_key = settings.OPENAI_API_KEY
        
        user_message = request.POST['user_message']
        
        # You can customize the prompt to guide the conversation
        prompt = f"User: {user_message}\nAI: " # Use f-strings instead of concatenating strings with +
                
        # create a chat completion
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
        
        ai_reply = chat_completion.choices[0].message.content.strip()

        return render(request, 'home_page.html', {'user_message': user_message, 'ai_reply': ai_reply})

    return render(request, 'home_page.html')