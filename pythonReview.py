def create_youtube_video(title, description):
	ytdict1={"title":title, "description":description, "likes":0,"dislikes":0,"comments" :{"username":""}}
	return ytdict1

def likes(video):
	if likes in video:
		video["likes"] += 1
		return video

def dislikes(ytdict1):
	if dislikes in video:
		video["dislikes"] += 1
		return video

def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username]= comment_text
	return youtubevideo

vid = create_youtube_video("WE CONTACTED AMONGUS GODS AT 3 AM!!(SCARY)","Craziest thing ever happened!! Watch and find out what happened")