import pandas as pd
import cv2

im = cv2.imread('/Users/anujkarn/Downloads/photo-1543466835-00a7907e9de1.webp')
col = 500
row = 500

new_shape = (col,row)
im = cv2.resize(im,new_shape)
blue,green,red = im[:,:,0], im[:,:,1], im[:,:,2]

op = pd.DataFrame(columns=['ColorId', 'Row', 'Col', 'Value'])

grayscale = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
grayscale = cv2.resize(grayscale, new_shape)


colors = [blue,green,red, grayscale]
id = 0
for r in colors:

    color_list = [id]*row*col

    row_list = []
    for i in range(row):
        row_list.extend([i]*col)

    col_list = list(range(col))*row

    val_list = r.reshape((1,row*col))[0]
    row_df = pd.DataFrame({
                'ColorId': color_list,
                'Row': row_list,
                'Col': col_list,
                'Value': val_list})

    op = pd.concat([op, row_df], ignore_index=True)
    id+=1

op.to_csv('output_img.csv')

