## ui
# pyside2-uic signin.ui > ui_signin.py

## resource
# pyrcc5 -o img_rc.py signin.qrc


scroll_bar = """
QScrollBar:vertical {  
    width:10px;   
    background-color:rgba(0,0,0,0%);   
    padding-top:10px;   
    padding-bottom:10px;  
}  

QScrollBar:horizontal {  
    height:10px;   
    background-color:rgba(0,0,0,0%);   
    padding-left:10px; padding-right:10px;  
}  

QScrollBar::handle:vertical {  
    width:10px;  
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD);   
}  

QScrollBar::handle:horizontal {  
    height:10px;  
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD);   
}  

QScrollBar::handle:vertical:hover {  
    width:10px;  
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5);   
}  

QScrollBar::handle:horizontal:hover {  
    height:10px;  
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5);   
}  

QScrollBar::add-line:vertical {  
    height:10px;  
    width:10px;  
    subcontrol-position: bottom;   
    subcontrol-origin: margin;  
    border-image:url(:/image/add-line_vertical.png);  
}  

QScrollBar::add-line:horizontal {  
    height:10px;  
    width:10px;  
    subcontrol-position: right;  
    subcontrol-origin: margin;  
    border-image:url(:/image/add-line_horizontal.png);  
}  

QScrollBar::sub-line:vertical {  
    height:10px;  
    width:10px;  
    subcontrol-position: top;   
    subcontrol-origin: margin;  
    border-image:url(:/image/sub-line_vertical.png);  
}  

QScrollBar::sub-line:horizontal {  
    height:10px;  
    width:10px;  
    subcontrol-position: left;  
    subcontrol-origin: margin;  
    border-image:url(:/image/sub-line_horizontal.png);  
}  

QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical {  
    width:10px;  
    background: #C0C0C0;  
}  

QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {  
    height:10px;  
    background: #C0C0C0;  
}
"""

