# Utilizing Python in Techncial Writing Tasks

## Library
python-docx <br>
Install: 
`
pip install python-docx
`
## Basic Word Structure
|        [0]        |     [1]      |         [2]       |
|       :---:       |    :---:     |        :---:      |
| simplicity is the | **ultimate** | *sophistication*. |
| RUN | RUN | RUN |

RUN object: a contiguous run of text with the same style.
## Import
```
import docx
doc = docx.Document('filename.docx')
```
## Show paragraph/run text 
### Show 1st paragraph text: <br>
`doc.paragraph[0].text` <br>
### Show the text of the 1st run in 1st paragraph: <br>
`doc.paragraph[0].run[0].text` <br>

## Check number of units (paragraph, run)
### Number of paragraphs: <br>
`len(doc.paragraphs)` <br>
### Number of runs in a paragraph: <br>
`len(doc.paragraphs[0].runs` <br>



