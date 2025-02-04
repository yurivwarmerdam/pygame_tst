# pygame_tst

## Some notes:
- [pytmx](https://pytmx.readthedocs.io/en/latest/). Allows loading of tilemaps into pygame. [code snippet at this video timestamp](https://youtu.be/N6xqCwblyiw?t=4793)
- [pydew valley](https://www.youtube.com/llkwatch?v=T4IX36sP_0c) Steal this liberally

## BehaviorTree.cpp install notes:
- [behaviorTrees.cpp website](https://www.behaviortree.dev/)  
- [BehaviorTree.cpp github repo](https://github.com/BehaviorTree/BehaviorTree.CPP?tab=readme-ov-file)  

all installs have been done from source.  

## command cheat sheet:
```
sudo apt install -y libczmq-dev libsqlite3-dev sqlite3 libgtest-dev

cmake BehaviorTree.CPP -S src/BehaviorTree.CPP -B build/BehaviorTree.CPP

cmake -DCMAKE_PREFIX_PATH=/c/dev/c/btrees/build/BehaviorTree.CPP simple_bt.CPP -S src/simple_bt -B build/simple_bt

cmake simple_bt.CPP -S src/simple_bt -B build/simple_bt

DISPLAY=:0 terminator &

ldd <some.so> # check dependencies of some.so file.

export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/include/python3.12 #before making, because boost needs this crap.
export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/include/x86_64-linux-gnu/python3.12

export CPLUS_INCLUDE_PATH=/usr/include/x86_64-linux-gnu/python3.12:/usr/include/python3.12
export CPLUS_INCLUDE_PATH=/usr/include/python3.12:/usr/include/x86_64-linux-gnu/python3.12

```
### C Links:

[The Intian guy tutorial](https://www.youtube.com/watch?v=4PUiDmD5dkg)  

[Sample Project](https://github.com/BehaviorTree/btcpp_sample)

[Official Tutorials](https://www.behaviortree.dev/docs/category/tutorials-basic/)

- [General intro to BTrees](https://www.youtube.com/watch?v=DCZJUvTQV5Q)  
- [one OOP BTree implementation on pytthon](https://iq.opengenus.org/b-tree-in-python/)  
- [pytrees](https://py-trees.readthedocs.io/en/devel/introduction.html)  

### pygame links:
[ultimate pygame tutorial by clear code.](https://youtu.be/AY9MnQ4x3zk?t=3556)  Timecode is at where I left off before wandering off to do my own thing.  
[Pygame Platformer tutorial by dafluffypotato](https://youtu.be/2gABYM5M0ww?t=4539)  Timecode is at where I left off before wandering off to do my own thing. 
[Sprites and Group explained](https://www.youtube.com/watch?v=4TfZjhw0J-8)  
[official tutorial on Tiles](https://pygame.readthedocs.io/en/latest/tiles/tiles.html)  
[that one dirtysprite explanation](https://n0nick.github.io/blog/2012/06/03/quick-dirty-using-pygames-dirtysprite-layered/)  
  
[Isometric rendering](https://www.youtube.com/watch?v=gE2gTCwLdFM)  
[Some spritesheet implementation](https://darth-data410.medium.com/how-to-easily-implement-sprite-sheets-in-your-pygames-120ce5ea9780)  

### other:
[Terminator cheat sheet](https://linuxsimply.com/wp-content/uploads/2023/05/Terminator-Cheat-Sheet-by-linuxsimply.pdf)
