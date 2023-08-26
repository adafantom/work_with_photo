from PIL import Image
import os




for image_number in range(5):
  
  
    image = Image.open("photo_{}.jpg".format(image_number))

    photo_vk = image.resize((1400, 1000))
    photo_inst = image.resize((1080, 1080))
    photo_inst = photo_inst.crop((10, 0, photo_inst.width-10, photo_inst.height))
    photo_fb = image.resize((1200, 628))


    file_path = "photo_end_{}".format(image_number)
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
  
    photo_vk.save('photo_end_{}/photo_vk.png'.format(image_number), 'png')
    photo_inst.save('photo_end_{}/photo_inst.png'.format(image_number), 'png')
    photo_fb.save('photo_end_{}/photo_fb.png'.format(image_number), 'png')