# Project Overview
A GUI that displays flash cards to aid the learning of the most common Spanish words.

# Objectives
- Get word list.
- Build User Interface.
- Setup a feature that allows the user to display the next word. 
- Design functionality that automatically flips the card to display the English translation after a set amount of time.
- Create a save feature for the unknown words.
- When the app is restarted, only unknown words would be shown.


# Results

Front Card

![2023-09-15 (7)](https://github.com/frantzalexander/flash-cards/assets/128331579/be62cacf-9ec0-461b-a8a2-2df66285e51e)


Back Card

![2023-09-15 (8)](https://github.com/frantzalexander/flash-cards/assets/128331579/aec6f45d-9cf7-43bb-a61a-40f8b3669e98)


# Process
```mermaid
flowchart TD
start(((START)))
ui{Build User Interface}
cross_button[Cross Button]
flip[Display English Translation]
check_button[Check Button]
next[Display Next Word]
save[Save Word Feature]
finish(((END)))
start --> ui
ui -->|Word Unknown|flip
flip --> cross_button
cross_button --> save
save --> finish
ui -->|Word Known|check_button
check_button --> next
next --> finish
