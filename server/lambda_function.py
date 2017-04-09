#import PIL import Image
import boto3

def lambda_handler(event, context):
    # TODO implement
    try:
        location = event["image"].index("base64") + 7
        str = event["image"][location:]
        fh = open("/tmp/image.png", "wb")
        fh.write(str.decode('base64'))
        fh.close()
        print "image:",str
        return str
    except:
        return "No image provided"
