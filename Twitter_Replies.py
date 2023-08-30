# import tweepy;
# import time;
# from PIL import Image;
# import os;
# import requests;
# import io;
# import re;
# from dotenv import load_dotenv;

# load_dotenv()
# api_key= os.environ.get("API_KEY")
# api_secret= os.environ.get("API_KEY_SECRET")
# bearer_token=os.environ.get("BEARER_TOKEN")
# access_token=os.environ.get("ACCESS_TOKEN")
# access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET")

# auth = tweepy.OAuthHandler(api_key,api_secret)
# auth.set_access_token(access_token,access_token_secret)
# client = tweepy.Client(bearer_token, api_key,api_secret,access_token,access_token_secret)
# api = tweepy.API(auth)

# bot_id = int(api.verify_credentials().id_str)



# def save_image_from_url(url, filename):
#     print("Begining Save Routine")
#     response = requests.get(url)
    
#     image = Image.open(io.BytesIO(response.content))
#     image.convert('RGB').save(filename, 'JPEG')
#     print("File Saved")



# def edit_image(background_path, foreground_path, output_path, transparency = 0.1):
#       # Open the background and foreground images
#     extra_file =0
#     bg = Image.open(background_path)
#     fg = Image.open(foreground_path)
    
#     # Check if image is JPG
#     if bg.format != 'JPEG':
#         new_path = '.'.join(background_path.split('.')[:-1]) + '.jpg'
#         bg.convert('RGB').save(new_path, 'JPEG')
#         bg = Image.open(new_path)
#         extra_file=1  #flag extra file

#     # Convert foreground image to have an alpha channel
#     alphafg = Image.new('L', fg.size, 178)
#     fg.putalpha(alphafg)

#     # # Apply transparency to foreground
#     if transparency:
#         fg = fg.point(lambda p: p * (1 - transparency) if p < 256 else 255)
    

#     # Overlay the foreground onto the background
#     left=(bg.width-400)/2
#     right =(bg.width+400)/2
#     top = (bg.height-400)/2
#     bot = (bg.height+400)/2
#     bg=bg.crop((left,top,right,bot))
#     bg.paste(fg, (0,0),fg)

#     # Save the result
#     bg.save(output_path, "JPEG")
#     # bg.show()

#     # Check and delete any extra files
#     if extra_file:
#         os.remove(new_path)
#         os.remove(background_path)

# with open('./mentionID.txt', 'r') as file:
#     mention_id = int(file.read())

# filename="./img/temporary.jpg"
# client_id = client.get_me().data.id
# request_counter=0
# username_pattern = r"^(?:@[A-Za-z0-9_]+ ?)+\d+$"

# while True:
#     response = client.get_users_mentions(client_id, since_id=mention_id,expansions=["author_id","in_reply_to_user_id"],user_fields=["id","profile_image_url"])
#     request_counter+=1
#     print(request_counter)
#     if response.data != None:
#         for mention in reversed(response.data):
#             print("Mention Tweet Found!")
#             mention_id=mention.id
#             print("Mention ID")
#             print(mention_id)

#             with open('./mentionID.txt', 'w') as file:
#                 file.write(str(mention_id))

            
#             try:
#                 if mention.in_reply_to_user_id != client_id:
#                     if mention.in_reply_to_user_id:
#                         if re.match(username_pattern, mention.text):
#                             label = re.findall(r'(?<!\w)\d+(?!\w)', mention.text)
#                             for num in label:
#                                 if int(num) >0 and int(num)<16:
                                
#                                     print("inside")

#                                     caller_profile = api.get_user(user_id=mention.in_reply_to_user_id)
#                                     image_url = caller_profile.profile_image_url_https.replace('_normal','')
#                                     print(image_url)

#                                     overlay= "./img/" +num+".jpg"
#                                 # # Grab Image and edit it.
#                                     save_image_from_url(image_url, filename)
#                                     edit_image(filename,overlay,"./img/Complete.jpg")
                                    
#                                     media = api.media_upload("./img/Complete.jpg")
#                                     client.create_tweet(in_reply_to_tweet_id=mention_id, media_ids= [media.media_id])
#                                     break
                            

#             except Exception as error:
#                 print("Error Occurred")
#                 print(error)
            

       
        
#     time.sleep(60)

