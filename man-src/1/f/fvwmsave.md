---
title: "fvwmsave(1)"
name: "fvwmsave"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmsave/"
---

FvwmSave - the Fvwm desktop-layout saving module 

<h2>Synopsis</h2>FvwmSave is spawned by fvwm, so no command line invocation will work. 

<h2>Description</h2>When called, this module will attempt to save your current desktop layout into a file called new.xinitrc. Ideally, this file will look just like .xinitrc, but in reality, you will have to edit it to get a usable configuration, so be sure to keep a backup of your old .xinitrc. 

 Your applications must supply certain hints to the X window system. Emacs, for example, does not, so FvwmSave can't get any information from it. 

 Also, FvwmSave assumes that certain command line options are globally accepted by applications, which may not be the case.
