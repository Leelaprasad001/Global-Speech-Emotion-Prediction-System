<h1>****** SPEECH EMOTION DETECTION ******</h1>
<br>
<center>PYTHON--------JUPYTER--------FRONTEND---------DEPLOYMENT-(FLASK)</center>
<br>
<BR>
<H2>ABOUT</H2>
<H2>Speech emotion detection is the process of analyzing audio data to determine the emotional state of the speaker, often using machine learning algorithms.</H2>
<BR>
<H4>IN THIS APPLICATION WE DETECT THE EMOTION OF TEXT BY USING MODELS.</H4>
<h4>In this project we are given a dataset along with the four labels which are classified into Joy and Netural and Optimism and Upset. we had trained the given dataset by using NLP methods and algorithms.<h4>
<H4>ENVIROMENT USED IS JUPYTER</H4>
<br>
<h3><b>Libraries used for the project</b></h3>

<ul type=disk>
<li>pandas</li>
<li>numpy</li>
<li>matplotlib</li>
<li>nltk</li>
<li>sklearn</li>
<li>genism</li>
<li>re</li>
<li>svm</li>
<li>GaussianNB</li>
<li>MultinomialNB</li>
<li>DecisionTreeClassifier</li>
<li>KNeighborsClassifier</li>
<li>RandomForestClassifier</li>
<li>LogisticRegression</li>
<li>TfidfVectorizer</li>
</ul>
<br>
<H3>This application uses the datasets, to find the legitimate emotion for the text given.
</h3>

<ol>
 <li>Loading dataset</li>
 <li>Preprocessing</li>
 <li>Word embedding</li>
 <li>Training</li>
 <li>Testing</li>
 <li>Deployment</li>
</ol>

<br>
<h2>Preprocessing</h2>
<h4>Preprocessing is crucial in Natural Language Processing (NLP) because it enhances the quality and usability of textual data for machine learning and language analysis tasks. Raw text data often contains various inconsistencies, noise, and irrelevant information that can hinder the accuracy and effectiveness of NLP models.</h4>

<h3>Steps done for Preprocesing</h3>
<ul type=disk>
<li>Tokenization : Break the text into individual words or tokens.</li>
<li>Lowercasing : Convert all text to lowercase to ensure consistency in text analysis.</li>
<li>Stopword Removal : Eliminate common words (e.g., "the," "and") that don't carry significant meaning.</li>
<li>Stemming or Lemmatization : Reduce words to their base or root form (e.g., "running" to "run") to normalize variations.</li>
<li>Removing Special Characters and Punctuation: Strip out non-alphanumeric characters and punctuation marks for cleaner text.</li>
<li>Removing Extra Whitespace : Remove extra whitespace between words and sentences to clean up the text.</li>
<li>Removing Numbers : Remove integers and other numerical characters to clean up the text.</li>
</ul>
<br>

<h3>Word Embedding Algorithms</h3>

<ol type=disk>
<li>TfidfVectorizer :  is a great tool provided by the scikit-learn library in Python. It is used to transform a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text.</li>
<li>Word2Vec : is a popular NLP technique that represents words as dense vector embeddings in a continuous vector space, capturing semantic relationships between words and enabling machine learning models to understand word context and similarities.</li>
<li>GloVe (Global Vectors for Word Representation) : is a word embedding technique in NLP that maps words to dense vectors based on their co-occurrence statistics, capturing semantic relationships and improving the efficiency of natural language understanding tasks.</li>
<!-- <li></li>
<li></li> -->
</ol>


<H2>RESULTS</H2>
 <!-- <br>
  <h3>USED CLASSIFIERS ARE:</h3>
  <table>
    <tr>
    <td>Classifier</td>
    <td>Metrics-MCC</td>
    <td>Metrics-ACCURACY</td>
    </tr>
    <TR>
      <td>MultinomialNB</td>
      <td>85.76719103708573</td>
      <td>93.87930464670501</td>
     </tr>
    <TR>
      <td>LogisticRegression</td>
      <td>78.84875639270138</td>
      <td>90.92471412519004</td>
     </tr>
    <TR>
      <td>KNeighborsClassifier</td>
      <td>79.35970411705305</td>
      <td>91.09656950228039</td>
     </tr>
    <TR>
      <td>GradientBoostingClassifier</td>
      <td>59.30651210477634</td>
      <td>82.89378015731377</td>
     </tr>
    <TR>
      <td>CatBoostClassifier</td>
      <td>72.72581200169554</td>
      <td>88.32044418005156</td>
     </tr>
  </table> -->


 <H3>FINALLY WE USED THE CLASSIFIER logistic regression GOT AN aacuracy .7</H3>
 <H3>DEPLOYED BY USING FLASK</H3>
  <H3>HOPE YOU UNDERSTAND</H3>  
     

