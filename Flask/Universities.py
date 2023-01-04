unames = ['University of Texas, Dallas',
    'NYU Tandon School of Engineering',
    'University of Michigan, Ann Arbor',
    'Western University',
    'University of California, San Diego',
    'Indiana University, Bloomington',
    'State University of New York, Buffalo',
    'University of Maryland, College Park',
    'University of Maryland, Baltimore County',
    'Harvard University',
    'Stanford University',
    'Illinios Institute of Technology, Chicago',
    'North Carolina State University',
    'University of Texas, Austin',
    'Kansas State University',
    'University of Massachusetts, Amherst',
    'University of Arizona',
    'University of Texas, Arlington',
    'New York University',
    'Texas A&M University, College Station',
    'Virginia Tech University',
    'University of Dayton, Ohio',
    'University of Illinois, Chicago',
    'Oklahoma State University, Stillwater',
    'San Jose State University',
    'University of South Carolina, Columbia',
    'Pennsylvania State University',
    'Western Michigan University']

filenames = []
for uname in unames:
    result = uname.replace(' ', '_')
    filena = 'model_' + result + '_XGBoost.pkl'
    filenames.append(filena)
