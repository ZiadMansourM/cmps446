% This is matlab code
first=1024;
second=first*3;

RGB=reshape(ones(first,1)*reshape(jet(first),1,second),[first,first,3]);
HSV=rgb2hsv(RGB);
H=HSV(:,:,1);
S=HSV(:,:,2);
V=HSV(:,:,3);
imshow(H)
figure, imshow(S);
figure, imshow(V);
figure, imshow(RGB);