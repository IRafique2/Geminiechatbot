import google.generativeai as genai

#add apikey here
API_KEY="AIzaSyDXuiZzPCmavxg2DH7NN5_rvKO5nM0xNaA"
genai.configure(api_key=[API_KEY])
#initialize model
model = genai.GenerativeModel('gemini-1.5-flash')
#create a function to get response
def GetResponseFromModel(user_input):
    response = model.generate_content(user_input)
    response.text

user_input=input("Enter a prompt =")
output=GetResponseFromModel(user_input)