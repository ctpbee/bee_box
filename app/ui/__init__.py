## ui
# pyside2-uic signin.ui > ui_signin.py


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
}  

QScrollBar::add-line:horizontal {  
    height:10px;  
    width:10px;  
    subcontrol-position: right;  
    subcontrol-origin: margin;  
}  

QScrollBar::sub-line:vertical {  
    height:10px;  
    width:10px;  
    subcontrol-position: top;   
    subcontrol-origin: margin;  
}  

QScrollBar::sub-line:horizontal {  
    height:10px;  
    width:10px;  
    subcontrol-position: left;  
    subcontrol-origin: margin;  
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

qss = """

QWidget{
background:#FFFFFF;
color:#000000
}

  
QProgressBar::chunk {  
    width: 5px;   
    margin: 0.5px;  
    background-color: #1B89CA;  
} 

QPushButton,QToolButton{
    border:1px solid #1b89ca;
    border-radius:5px;
    padding:5px
}
QPushButton:disabled{
    background:#2B2B2B;
    color:#b6b6b6;
}
QToolButton:down-arrow{
    border-radius:15px;

}

QPushButton:hover,QToolButton:hover{
    background:#BFE2F5;
}


QMenu::item:selected{
    background: #BFE2F5;
    color: black;
}


QTabBar::tab {
     border:1px solid #1b89ca;
     border-radius:2px;
     min-width: 60px;
     padding: 2px;
 }
QTabBar::tab:selected{
    background:#1b89ca;
}
QTabBar::tab:!selected{
    margin-top:5px;
}

QTabWidget::pane{
    border:1px solid #1b89ca;
}


QComboBox,QLineEdit,QDoubleSpinBox,QSpinBox{
    color:#000000;
    border:1px solid #1b89ca;
    border-radius:5px;
}

QComboBox:disabled,QLineEdit:disabled,QDoubleSpinBox:disabled,QSpinBox:disabled,QPushButton:disabled{
    background:#2B2B2B;
}

QToolButton::drop-down{
border-top-right-radius: 3px;
border-bottom-right-radius: 3px;
}
""" + scroll_bar
