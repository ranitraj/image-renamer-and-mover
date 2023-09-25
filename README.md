# image-renamer-and-mover
Renames the image based on the expected format &amp; moves them into the desired target folder

## Steps to use:
1. Move the dataset folder into the same project directory in which the script exists. For instance, replace the test directory with the desired directory. Ensure that it remains in the same format as shown below.
```
test/575/575-70-01-0019-01/8/2023-05-24/positive
test/575/575-70-01-0019-01/8/2023-05-24/positive
```
2. Inside main function, replace the root_direcotry with the name of the directory from the first step.
```
 root_directory = './test'   # replace with own
```
3. Also, replace the variables target_positive_directory and target_negative_directory with the path in which you want to save the final directories.
```
target_positive_directory = '/Users/ranitrajganguly/Desktop/thermal_dataset/positive'   # replace with own
target_negative_directory = '/Users/ranitrajganguly/Desktop/thermal_dataset/negative'   # replace with own
```
4. Run the main.py file or execute the same via terminal inside the IDE. In running via system terimal, replace with absolute path.
```
python main.py
```

## Possible Error:
If the follwing error is encountered while execution:
```
OSError: [Errno 30] Read-only file system: '/thermal_dataset'
```
Run the script as Root user using:
```
sudo python main.py
```

