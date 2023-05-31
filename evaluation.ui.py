<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QDialog" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>652</width>
    <height>663</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <layout class="QGridLayout" name="gridLayout">
   <item row="1" column="0">
    <widget class="QLabel" name="label_3">
     <property name="font">
      <font>
       <pointsize>14</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="contextMenuPolicy">
      <enum>Qt::NoContextMenu</enum>
     </property>
     <property name="text">
      <string>Evaluation of performance</string>
     </property>
    </widget>
   </item>
   <item row="7" column="0">
    <layout class="QHBoxLayout" name="horizontalLayout_3">
     <item>
      <widget class="QListView" name="listView"/>
     </item>
     <item>
      <spacer name="horizontalSpacer_2">
       <property name="orientation">
        <enum>Qt::Horizontal</enum>
       </property>
       <property name="sizeType">
        <enum>QSizePolicy::Fixed</enum>
       </property>
       <property name="sizeHint" stdset="0">
        <size>
         <width>120</width>
         <height>20</height>
        </size>
       </property>
      </spacer>
     </item>
     <item>
      <widget class="QListView" name="listView_2"/>
     </item>
    </layout>
   </item>
   <item row="5" column="0">
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QLabel" name="label">
       <property name="font">
        <font>
         <pointsize>10</pointsize>
         <weight>75</weight>
         <bold>true</bold>
        </font>
       </property>
       <property name="text">
        <string>Players</string>
       </property>
      </widget>
     </item>
     <item>
      <spacer name="horizontalSpacer_3">
       <property name="orientation">
        <enum>Qt::Horizontal</enum>
       </property>
       <property name="sizeType">
        <enum>QSizePolicy::Fixed</enum>
       </property>
       <property name="sizeHint" stdset="0">
        <size>
         <width>300</width>
         <height>20</height>
        </size>
       </property>
      </spacer>
     </item>
     <item>
      <widget class="QLabel" name="label_2">
       <property name="font">
        <font>
         <pointsize>10</pointsize>
         <weight>75</weight>
         <bold>true</bold>
        </font>
       </property>
       <property name="text">
        <string>Points</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="lineEdit_8"/>
     </item>
    </layout>
   </item>
   <item row="4" column="0">
    <spacer name="verticalSpacer_2">
     <property name="orientation">
      <enum>Qt::Vertical</enum>
     </property>
     <property name="sizeType">
      <enum>QSizePolicy::Fixed</enum>
     </property>
     <property name="sizeHint" stdset="0">
      <size>
       <width>20</width>
       <height>5</height>
      </size>
     </property>
    </spacer>
   </item>
   <item row="6" column="0">
    <spacer name="verticalSpacer_3">
     <property name="orientation">
      <enum>Qt::Vertical</enum>
     </property>
     <property name="sizeType">
      <enum>QSizePolicy::Fixed</enum>
     </property>
     <property name="sizeHint" stdset="0">
      <size>
       <width>20</width>
       <height>5</height>
      </size>
     </property>
    </spacer>
   </item>
   <item row="2" column="0">
    <spacer name="verticalSpacer">
     <property name="orientation">
      <enum>Qt::Vertical</enum>
     </property>
     <property name="sizeType">
      <enum>QSizePolicy::Fixed</enum>
     </property>
     <property name="sizeHint" stdset="0">
      <size>
       <width>20</width>
       <height>5</height>
      </size>
     </property>
    </spacer>
   </item>
   <item row="9" column="0">
    <widget class="QPushButton" name="pushButton_1">
     <property name="font">
      <font>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>Calculate Score</string>
     </property>
    </widget>
   </item>
   <item row="3" column="0">
    <layout class="QHBoxLayout" name="horizontalLayout_2">
     <item>
      <widget class="QComboBox" name="comboBox">
       <property name="enabled">
        <bool>true</bool>
       </property>
       <property name="contextMenuPolicy">
        <enum>Qt::DefaultContextMenu</enum>
       </property>
       <property name="insertPolicy">
        <enum>QComboBox::InsertAtBottom</enum>
       </property>
       <property name="sizeAdjustPolicy">
        <enum>QComboBox::AdjustToContentsOnFirstShow</enum>
       </property>
      </widget>
     </item>
     <item>
      <spacer name="horizontalSpacer">
       <property name="orientation">
        <enum>Qt::Horizontal</enum>
       </property>
       <property name="sizeType">
        <enum>QSizePolicy::Fixed</enum>
       </property>
       <property name="sizeHint" stdset="0">
        <size>
         <width>120</width>
         <height>20</height>
        </size>
       </property>
      </spacer>
     </item>
     <item>
      <widget class="QComboBox" name="comboBox_2"/>
     </item>
    </layout>
   </item>
   <item row="8" column="0">
    <spacer name="verticalSpacer_4">
     <property name="orientation">
      <enum>Qt::Vertical</enum>
     </property>
     <property name="sizeType">
      <enum>QSizePolicy::Fixed</enum>
     </property>
     <property name="sizeHint" stdset="0">
      <size>
       <width>20</width>
       <height>5</height>
      </size>
     </property>
    </spacer>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
