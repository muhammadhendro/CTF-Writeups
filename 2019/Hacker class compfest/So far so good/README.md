# So far so good

diberikan file zip berulang yang diekstrak juga menghasilkan sebuah base64 <br>
script berikut <br>

```
import zipfile, re, os
    def extract_nested_zip(zippedFile, toFolder):
        """ Unzip a zip file and its contents, including nested zip files
            Delete the zip file(s) after extraction
        """
        with zipfile.ZipFile(zippedFile, 'r') as zfile:
            zfile.extractall(path=toFolder)
        os.remove(zippedFile)
        for root, dirs, files in os.walk(toFolder):
            for filename in files:
                if re.search(r'\.zip$', filename):
                    fileSpec = os.path.join(root, filename)
                    extract_nested_zip(fileSpec, root)

    

     extract_nested_zip("P.zip","/root/Unduhan/hacker class compfest/")

```
hasil dir base64<br>
```
/root/Unduhan/hacker class compfest/P/G/F/1/d/G/h/v/c/i/B/h/c/m/l/x/Y/m/F/z/e/W/F/y/P/i/B/h/a/C/B/p/I/H/N/l/Z/S/B/5/b/3/V/y/I/G/h/h/c/m/Q/g/d/2/9/y/a/y/w/g/a/G/V/y/Z/S/B/p/c/y/B/5/b/3/V/y/I/G/Z/s/Y/W/c/g/Q/0/9/N/U/E/Z/F/U/1/Q/x/M/X/t/i/Y/X/M/z/X/3/N/p/e/H/R/5/X/2/Y/w/d/X/J/f/Y/X/R/f/M/X/R/z/X/2/Z/p/b/m/V/z/d/H/0/= 
```
decode <br>
```
<author ariqbasyar> ah i see your hard work, here is your flag ``` **COMPFEST11{bas3_sixty_f0ur_at_1ts_finest}**
