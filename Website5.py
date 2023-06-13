
import streamlit as st
from streamlit_echarts import st_echarts
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components


st.set_page_config(page_title="Amazon Sentimentanalyse", page_icon=":tada", layout="centered")

col1, col2, = st.columns(2)


with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "Contact"],
        icons=["house", "book", "envelope"],
    )

if selected == "Home":
    tab1, tab2, tab3 = st.tabs(["Deskriptive Analyse", "Text Analyse", "Sentimentanalyse"])
    
    
    with tab1:
    

      options = {
          "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
          "legend": {
              "data": ["Direct", "Mail Ad", "Affiliate Ad", "Video Ad", "Search Engine"]
          },
          "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
          "xAxis": {"type": "value"},
          "yAxis": {
              "type": "category",
              "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
          },
          "series": [
              {
                  "name": "Direct",
                  "type": "bar",
                  "stack": "total",
                  "label": {"show": True},
                  "emphasis": {"focus": "series"},
                  "data": [320, 302, 301, 334, 390, 330, 320],
              },
              {
                  "name": "Mail Ad",
                  "type": "bar",
                  "stack": "total",
                  "label": {"show": True},
                  "emphasis": {"focus": "series"},
                  "data": [120, 132, 101, 134, 90, 230, 210],
              },
              {
                  "name": "Affiliate Ad",
                  "type": "bar",
                  "stack": "total",
                  "label": {"show": True},
                  "emphasis": {"focus": "series"},
                  "data": [220, 182, 191, 234, 290, 330, 310],
              },
              {
                  "name": "Video Ad",
                  "type": "bar",
                  "stack": "total",
                  "label": {"show": True},
                  "emphasis": {"focus": "series"},
                  "data": [150, 212, 201, 154, 190, 330, 410],
              },
              {
                  "name": "Search Engine",
                  "type": "bar",
                  "stack": "total",
                  "label": {"show": True},
                  "emphasis": {"focus": "series"},
                  "data": [820, 832, 901, 934, 1290, 1330, 1320],
              },
          ],
      }
      st_echarts(options=options, height="500px")

    
    with tab2:   

        st.write("Hier steht Text3Text3")
      # Werte für die Diagrammkonfiguration
        pos = "insideBottom"
        rotate = 90
        align = "left"
        vertical_align = "middle"
        distance = 15

        label_option = {
          "show": True,
          "position": pos,
          "distance": distance,
          "align": align,
          "verticalAlign": vertical_align,
          "rotate": rotate,
          "formatter": "{c}  {name|{a}}",
          "fontSize": 16,
          "rich": {
            "name": {}
          }
        }

        options = {
          "tooltip": {
            "trigger": "axis",
            "axisPointer": {
              "type": "shadow"
            }
          },
          "legend": {
            "data": ["Forest", "Steppe", "Desert", "Wetland"]
          },
          "toolbox": {
            "show": True,
            "orient": "vertical",
            "left": "right",
            "top": "center",
            "feature": {
              "mark": {"show": True},
              "dataView": {"show": True, "readOnly": False},
              "magicType": {"show": True, "type": ["line", "bar", "stack"]},
              "restore": {"show": True},
              "saveAsImage": {"show": True}
            }
          },
          "xAxis": [
            {
              "type": "category",
              "axisTick": {"show": True},
              "data": ["2012", "2013", "2014", "2015", "2016"]
            }
          ],
          "yAxis": [
            {
              "type": "value"
            }
          ],
          "series": [
            {
              "name": "Forest",
              "type": "bar",
              "barGap": 0,
              "label": label_option,
              "emphasis": {
                "focus": "series"
              },
              "data": [320, 332, 301, 334, 390]
            },
            {
              "name": "Steppe",
              "type": "bar",
              "label": label_option,
              "emphasis": {
                "focus": "series"
              },
              "data": [220, 182, 191, 234, 290]
            },
            {
              "name": "Desert",
              "type": "bar",
              "label": label_option,
              "emphasis": {
                "focus": "series"
              },
              "data": [150, 232, 201, 154, 190]
            },
            {
              "name": "Wetland",
              "type": "bar",
              "label": label_option,
              "emphasis": {
                "focus": "series"
              },
              "data": [98, 77, 101, 99, 40]
            },

            {
                "name": "Red Line",
                "type": "line",
                "data": [200, 200, 200, 200, 200],
                "itemStyle": {"color": "red"},
                "lineStyle": {"width": 2},
                "markLine": {
                    "silent": True,
                    "data": [{"yAxis": 200}]
                }
            }
        ]
        }

        # Zeichnen des Diagramms
        st_echarts(options=options, height="600px")
      
      
        st.write("Hier steht Text2222 Text2")


    with tab3:
      st.write("Hier steht Text2")


if selected == "Projects":
   
  # Werte für die Diagrammkonfiguration
  pos = "insideBottom"
  rotate = 90
  align = "left"
  vertical_align = "middle"
  distance = 15

  label_option = {
    "show": True,
    "position": pos,
    "distance": distance,
    "align": align,
    "verticalAlign": vertical_align,
    "rotate": rotate,
    "formatter": "{c}  {name|{a}}",
    "fontSize": 16,
    "rich": {
      "name": {}
    }
  }

  options = {
    "tooltip": {
      "trigger": "axis",
      "axisPointer": {
        "type": "shadow"
      }
    },
    "legend": {
      "data": ["Forest", "Steppe", "Desert", "Wetland"]
    },
    "toolbox": {
      "show": True,
      "orient": "vertical",
      "left": "right",
      "top": "center",
      "feature": {
        "mark": {"show": True},
        "dataView": {"show": True, "readOnly": False},
        "magicType": {"show": True, "type": ["line", "bar", "stack"]},
        "restore": {"show": True},
        "saveAsImage": {"show": True}
      }
    },
    "xAxis": [
      {
        "type": "category",
        "axisTick": {"show": False},
        "data": ["2012", "2013", "2014", "2015", "2016"]
      }
    ],
    "yAxis": [
      {
        "type": "value"
      }
    ],
    "series": [
      {
        "name": "Forest",
        "type": "bar",
        "barGap": 0,
        "label": label_option,
        "emphasis": {
          "focus": "series"
        },
        "data": [320, 332, 301, 334, 390]
      },
      {
        "name": "Steppe",
        "type": "bar",
        "label": label_option,
        "emphasis": {
          "focus": "series"
        },
        "data": [220, 182, 191, 234, 290]
      },
      {
        "name": "Desert",
        "type": "bar",
        "label": label_option,
        "emphasis": {
          "focus": "series"
        },
        "data": [150, 232, 201, 154, 190]
      },
      {
        "name": "Wetland",
        "type": "bar",
        "label": label_option,
        "emphasis": {
          "focus": "series"
        },
        "data": [98, 77, 101, 99, 40]
      },

      {
          "name": "Red Line",
          "type": "line",
          "data": [200, 200, 200, 200, 200],
          "itemStyle": {"color": "red"},
          "lineStyle": {"width": 2},
          "markLine": {
              "silent": True,
              "data": [{"yAxis": 200}]
          }
      }



    ]
  }

  # Zeichnen des Diagramms
  st_echarts(options=options, height="500px")


html_string='''
<script>
// To break out of iframe and access the parent window
const streamlitDoc = window.parent.document;

// Make the replacement
document.addEventListener("DOMContentLoaded", function(event){
        streamlitDoc.getElementsByTagName("footer")[0].innerHTML = "Provided by Aenny, Cornelius, Tim and Alex";
    });
</script>
'''
components.html(html_string)
 