# -*- coding:utf8 -*-
import os
class BatchRename():
    '''
    批量重命名文件夹中的图片文件
    '''
    def __init__(self):
        self.path = '/home/sys418/桌面/LYY_file/nation_flag/nation_flag/xhdpi'
    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 0
        for item in filelist:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path), item)
                if i<10:
                    dst = os.path.join(os.path.abspath(self.path),'00' + str(i) + '.jpg')
                if i<100:
                    dst = os.path.join(os.path.abspath(self.path),'0' + str(i) + '.jpg')

                try:
                    os.rename(src, dst)
                    print 'converting %s to %s ...' % (src, dst)
                    i = i + 1
                except:
                    continue
        print 'total %d to rename & converted %d jpgs' % (total_num, i)
if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
