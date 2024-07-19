{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPHJi6jqOnS9QN88ZSz1KfM",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/samukelisiewenkosi/Team-EG4_Streamlit/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "YtwrGDzMmZY8"
      },
      "outputs": [],
      "source": [
        "! pip install streamlit -q"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!wget -q -O - ipv4.icanhazip.com"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y95hfSxGm_2A",
        "outputId": "09495117-77ba-48e9-e926-cee579d41e2d"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "34.125.205.180\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "! streamlit run app.py"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WwUFpJ4Hn0Me",
        "outputId": "08f05061-bf25-4250-ecb1-a44e1694bf9a"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Usage: streamlit run [OPTIONS] TARGET [ARGS]...\n",
            "Try 'streamlit run --help' for help.\n",
            "\n",
            "Error: Invalid value: File does not exist: app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "dFYbIKnuphjO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import joblib\n",
        "import pandas as pd\n",
        "from PyPDF2 import PdfReader\n",
        "import docx\n",
        "import re\n",
        "import nltk\n",
        "from nltk.corpus import stopwords\n",
        "from nltk.stem import WordNetLemmatizer\n",
        "from wordcloud import WordCloud\n",
        "import matplotlib.pyplot as plt\n"
      ],
      "metadata": {
        "id": "hOXVSKeXn0Gu"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "NE0DVU2Gnz0f"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}