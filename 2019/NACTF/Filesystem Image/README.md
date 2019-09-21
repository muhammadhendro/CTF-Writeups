# fsimage

lakukan mount<br>


```
sudo fdisk -l -u=sectors fsimage.iso
``` <br>

```
sudo mount -o loop,offset=512 fsimage.iso /mnt/
```
