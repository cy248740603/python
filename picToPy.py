import base64
def handle_pic_to_py(picture_name):
    open_pic = open('{}.png'.format(picture_name),'rb')
    b64str = base64.b64encode(open_pic.read())
    open_pic.close()
    write_data = 'img = "%s"' % b64str.decode()
    f = open('%s.py' % picture_name, 'w+')
    f.write(write_data)
    f.close()
if __name__=='__main__':
    picture = ['png_strawberry','bing','basketball','png_cxk','jpg_cxk']
    for picture_position in picture:
        handle_pic_to_py(picture_position)