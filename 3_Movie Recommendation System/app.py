import streamlit as st
import pickle
import pandas as pd
import requests

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# UI + recommend logic here
