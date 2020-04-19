function []= drawLeftRedSquare()
cgloadlib
cgopen(1,0,0,0)
cgscale(30)
cgalign('l','c')
cgpencol(1,0,0)%% colour change
cgrect(-6,-4,7,7)
cgflip
wait(5000)
end