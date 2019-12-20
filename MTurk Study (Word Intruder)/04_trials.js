// In this file you can specify the trial data for your experiment
const trial_list = {
  trials : [
   _.shuffle(['larry', 'michael', 'david', 'steve', 'cleveland', 'tom']),
   _.shuffle(['people', 'problem', 'solution', 'fact', 'agree', 'point']),
   _.shuffle(['faq', 'list', 'info', 'information', 'book', 'food']),
   _.shuffle(['reply', 'posting', 'article', 'problem', 'writes', 'wrote']),
   _.shuffle(['cleveland', 'point', 'object', 'line', 'convex', 'points']),
   _.shuffle(['stupid', 'brain', 'ac', 'mind', 'dyer', 'show']),
   _.shuffle(['hz', 'sl', 'writes', 'cx', 'wm', 'pl']),
   _.shuffle(['bob', 'yeah', 'folks', 'guess', 'wrong', 'doubt']),
   _.shuffle(['western', 'university', 'ohio', 'serdar', 'cwru', 'state']),
   _.shuffle(['hell', 'kill', 'die', 'area', 'person', 'death']),

   _.shuffle(['uk', 'toronto', 'tv', 'list', 'university', 'canada']),
   _.shuffle(['output', 'file', 'entry', 'max', 'window', 'program']),
   _.shuffle(['people', 'moral', 'evidence', 'argument', 'work', 'god']),
   _.shuffle(['digex', 'time', 'cso', 'acs', 'bnr', 'netcom']),
   _.shuffle(['guess', 'keith', 'jon', 'writes', 'brian', 'andrew']),
   _.shuffle(['cost', 'low', 'performance', 'high', 'rate', 'sale']),
   _.shuffle(['cs', 'hand', 'mine', 'case', 'made', 'tin']),
   _.shuffle(['system', 'mail', 'file', 'anonymous', 'internet', 'ftp']),
   _.shuffle(['work', 'works', 'bob', 'end', 'run', 'fine']),
   _.shuffle( ['att', 'dept', 'comp', 'cc', 'cs', 'tin']),

   _.shuffle(['fonts', 'printer', 'hp', 'print', 'david', 'oz']),
   _.shuffle(['people', 'jesus', 'bible', 'line', 'god', 'christ']),
   _.shuffle(['game', 'year', 'serdar', 'hockey', 'team', 'season']),
   _.shuffle(['au', 'mil', 'fi', 'org', 'eng', 'list']),
   _.shuffle(['air', 'game', 'space', 'power', 'nuclear', 'water']),
   _.shuffle(['bob', 'baseball', 'doug', 'gary', 'roger', 'tin']),
   _.shuffle(['question', 'opinions', 'high', 'true', 'agree', 'change']),
   _.shuffle(['gun', 'note', 'people', 'police', 'law', 'guns']),
   _.shuffle(['host', 'visgraph', 'netcom', 'university', 'shuldig', 'college']),
   _.shuffle( ['post', 'university', 'reply', 'posting', 'disclaimer', 'article']),

   _.shuffle(['opinions', 'sale', 'times', 'year', 'time', 'people']),
   _.shuffle(['high', 'livesey', 'day', 'work', 'place', 'pub']), //changed this because found intruder, "work", is in the list.
   _.shuffle(['made', 'time', 'people', 'make', 'hell', 'things']),
   _.shuffle(['fire', 'people', 'sale', 'children', 'killed', 'told']),
   _.shuffle(['keys', 'public', 'government', 'high', 'encryption', 'key']),
   _.shuffle(['keyboard', 'david', 'problem', 'mouse', 'screen', 'problems']),
   _.shuffle(['god', 'sera', 'flame', 'serdar', 'dseg', 'magnus']),
   _.shuffle(['patients', 'disease', 'health', 'medical', 'host', 'food']),
   _.shuffle(['david', 'michael', 'writes', 'air', 'mike', 'steve']),
   _.shuffle(['bj', 'tq', 'db', 'gun', 'max', 'qq']),

   _.shuffle(['circuit', 'power', 'ac', 'voltage', 'ground', 'guess']),
   _.shuffle(['system', 'unix', 'support', 'server', 'line', 'software']),
   _.shuffle(['wrong', 'guess', 'question', 'happened', 'times', 'thing']),
   _.shuffle(['computing', 'technical', 'computer', 'air', 'science', 'research']),
   _.shuffle(['sale', 'price', 'sell', 'advance', 'point', 'offer']),
   _.shuffle(['york', 'chicago', 'food', 'san', 'st', 'cleveland']),
   _.shuffle(['information', 'states', 'national', 'gun', 'conference', 'general']),
   _.shuffle(['area', 'reserve', 'midway', 'cross', 'semi', 'day']),
   _.shuffle(['company', 'local', 'distribution', 'line', 'news', 'group']),
   _.shuffle(['avoid', 'check', 'rules', 'note', 'article', 'case'])
  ]
}


const trial_info = {
    forced_choice: [
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[0][0],
            option2: trial_list.trials[0][1],
            option3: trial_list.trials[0][2],
            option4: trial_list.trials[0][3],
            option5: trial_list.trials[0][4],
            option6: trial_list.trials[0][5],
            correct: 'cleveland'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[1][0],
            option2: trial_list.trials[1][1],
            option3: trial_list.trials[1][2],
            option4: trial_list.trials[1][3],
            option5: trial_list.trials[1][4],
            option6: trial_list.trials[1][5],
            correct: 'people'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[2][0],
            option2: trial_list.trials[2][1],
            option3: trial_list.trials[2][2],
            option4: trial_list.trials[2][3],
            option5: trial_list.trials[2][4],
            option6: trial_list.trials[2][5],
            correct: 'food'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[3][0],
            option2: trial_list.trials[3][1],
            option3: trial_list.trials[3][2],
            option4: trial_list.trials[3][3],
            option5: trial_list.trials[3][4],
            option6: trial_list.trials[3][5],
            correct: 'problem'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[4][0],
            option2: trial_list.trials[4][1],
            option3: trial_list.trials[4][2],
            option4: trial_list.trials[4][3],
            option5: trial_list.trials[4][4],
            option6: trial_list.trials[4][5],
            correct: 'cleveland'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[5][0],
            option2: trial_list.trials[5][1],
            option3: trial_list.trials[5][2],
            option4: trial_list.trials[5][3],
            option5: trial_list.trials[5][4],
            option6: trial_list.trials[5][5],
            correct: 'ac'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[6][0],
            option2: trial_list.trials[6][1],
            option3: trial_list.trials[6][2],
            option4: trial_list.trials[6][3],
            option5: trial_list.trials[6][4],
            option6: trial_list.trials[6][5],
            correct: 'writes'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[7][0],
            option2: trial_list.trials[7][1],
            option3: trial_list.trials[7][2],
            option4: trial_list.trials[7][3],
            option5: trial_list.trials[7][4],
            option6: trial_list.trials[7][5],
            correct: 'bob'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[8][0],
            option2: trial_list.trials[8][1],
            option3: trial_list.trials[8][2],
            option4: trial_list.trials[8][3],
            option5: trial_list.trials[8][4],
            option6: trial_list.trials[8][5],
            correct: 'serdar'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[9][0],
            option2: trial_list.trials[9][1],
            option3: trial_list.trials[9][2],
            option4: trial_list.trials[9][3],
            option5: trial_list.trials[9][4],
            option6: trial_list.trials[9][5],
            correct: 'area'
        },

        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[10][0],
            option2: trial_list.trials[10][1],
            option3: trial_list.trials[10][2],
            option4: trial_list.trials[10][3],
            option5: trial_list.trials[10][4],
            option6: trial_list.trials[10][5],
            correct: 'list'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[11][0],
            option2: trial_list.trials[11][1],
            option3: trial_list.trials[11][2],
            option4: trial_list.trials[11][3],
            option5: trial_list.trials[11][4],
            option6: trial_list.trials[11][5],
            correct: 'max'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[12][0],
            option2: trial_list.trials[12][1],
            option3: trial_list.trials[12][2],
            option4: trial_list.trials[12][3],
            option5: trial_list.trials[12][4],
            option6: trial_list.trials[12][5],
            correct: 'work'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[13][0],
            option2: trial_list.trials[13][1],
            option3: trial_list.trials[13][2],
            option4: trial_list.trials[13][3],
            option5: trial_list.trials[13][4],
            option6: trial_list.trials[13][5],
            correct: 'time'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[14][0],
            option2: trial_list.trials[14][1],
            option3: trial_list.trials[14][2],
            option4: trial_list.trials[14][3],
            option5: trial_list.trials[14][4],
            option6: trial_list.trials[14][5],
            correct: 'guess'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[15][0],
            option2: trial_list.trials[15][1],
            option3: trial_list.trials[15][2],
            option4: trial_list.trials[15][3],
            option5: trial_list.trials[15][4],
            option6: trial_list.trials[15][5],
            correct: 'sale'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[16][0],
            option2: trial_list.trials[16][1],
            option3: trial_list.trials[16][2],
            option4: trial_list.trials[16][3],
            option5: trial_list.trials[16][4],
            option6: trial_list.trials[16][5],
            correct: 'cs'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[17][0],
            option2: trial_list.trials[17][1],
            option3: trial_list.trials[17][2],
            option4: trial_list.trials[17][3],
            option5: trial_list.trials[17][4],
            option6: trial_list.trials[17][5],
            correct: 'system'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[18][0],
            option2: trial_list.trials[18][1],
            option3: trial_list.trials[18][2],
            option4: trial_list.trials[18][3],
            option5: trial_list.trials[18][4],
            option6: trial_list.trials[18][5],
            correct: 'bob'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[19][0],
            option2: trial_list.trials[19][1],
            option3: trial_list.trials[19][2],
            option4: trial_list.trials[19][3],
            option5: trial_list.trials[19][4],
            option6: trial_list.trials[19][5],
            correct: 'tin'
        },

        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[20][0],
            option2: trial_list.trials[20][1],
            option3: trial_list.trials[20][2],
            option4: trial_list.trials[20][3],
            option5: trial_list.trials[20][4],
            option6: trial_list.trials[20][5],
            correct: 'david'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[21][0],
            option2: trial_list.trials[21][1],
            option3: trial_list.trials[21][2],
            option4: trial_list.trials[21][3],
            option5: trial_list.trials[21][4],
            option6: trial_list.trials[21][5],
            correct: 'line'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[22][0],
            option2: trial_list.trials[22][1],
            option3: trial_list.trials[22][2],
            option4: trial_list.trials[22][3],
            option5: trial_list.trials[22][4],
            option6: trial_list.trials[22][5],
            correct: 'serdar'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[23][0],
            option2: trial_list.trials[23][1],
            option3: trial_list.trials[23][2],
            option4: trial_list.trials[23][3],
            option5: trial_list.trials[23][4],
            option6: trial_list.trials[23][5],
            correct: 'list'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[24][0],
            option2: trial_list.trials[24][1],
            option3: trial_list.trials[24][2],
            option4: trial_list.trials[24][3],
            option5: trial_list.trials[24][4],
            option6: trial_list.trials[24][5],
            correct: 'game'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[25][0],
            option2: trial_list.trials[25][1],
            option3: trial_list.trials[25][2],
            option4: trial_list.trials[25][3],
            option5: trial_list.trials[25][4],
            option6: trial_list.trials[25][5],
            correct: 'tin'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[26][0],
            option2: trial_list.trials[26][1],
            option3: trial_list.trials[26][2],
            option4: trial_list.trials[26][3],
            option5: trial_list.trials[26][4],
            option6: trial_list.trials[26][5],
            correct: 'high'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[27][0],
            option2: trial_list.trials[27][1],
            option3: trial_list.trials[27][2],
            option4: trial_list.trials[27][3],
            option5: trial_list.trials[27][4],
            option6: trial_list.trials[27][5],
            correct: 'note'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[28][0],
            option2: trial_list.trials[28][1],
            option3: trial_list.trials[28][2],
            option4: trial_list.trials[28][3],
            option5: trial_list.trials[28][4],
            option6: trial_list.trials[28][5],
            correct: 'netcom'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[29][0],
            option2: trial_list.trials[29][1],
            option3: trial_list.trials[29][2],
            option4: trial_list.trials[29][3],
            option5: trial_list.trials[29][4],
            option6: trial_list.trials[29][5],
            correct: 'university'
        },

        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[30][0],
            option2: trial_list.trials[30][1],
            option3: trial_list.trials[30][2],
            option4: trial_list.trials[30][3],
            option5: trial_list.trials[30][4],
            option6: trial_list.trials[30][5],
            correct: 'sale'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[31][0],
            option2: trial_list.trials[31][1],
            option3: trial_list.trials[31][2],
            option4: trial_list.trials[31][3],
            option5: trial_list.trials[31][4],
            option6: trial_list.trials[31][5],
            correct: 'work'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[32][0],
            option2: trial_list.trials[32][1],
            option3: trial_list.trials[32][2],
            option4: trial_list.trials[32][3],
            option5: trial_list.trials[32][4],
            option6: trial_list.trials[32][5],
            correct: 'hell'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[33][0],
            option2: trial_list.trials[33][1],
            option3: trial_list.trials[33][2],
            option4: trial_list.trials[33][3],
            option5: trial_list.trials[33][4],
            option6: trial_list.trials[33][5],
            correct: 'sale'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[34][0],
            option2: trial_list.trials[34][1],
            option3: trial_list.trials[34][2],
            option4: trial_list.trials[34][3],
            option5: trial_list.trials[34][4],
            option6: trial_list.trials[34][5],
            correct: 'high'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[35][0],
            option2: trial_list.trials[35][1],
            option3: trial_list.trials[35][2],
            option4: trial_list.trials[35][3],
            option5: trial_list.trials[35][4],
            option6: trial_list.trials[35][5],
            correct: 'david'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[36][0],
            option2: trial_list.trials[36][1],
            option3: trial_list.trials[36][2],
            option4: trial_list.trials[36][3],
            option5: trial_list.trials[36][4],
            option6: trial_list.trials[36][5],
            correct: 'god'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[37][0],
            option2: trial_list.trials[37][1],
            option3: trial_list.trials[37][2],
            option4: trial_list.trials[37][3],
            option5: trial_list.trials[37][4],
            option6: trial_list.trials[37][5],
            correct: 'host'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[38][0],
            option2: trial_list.trials[38][1],
            option3: trial_list.trials[38][2],
            option4: trial_list.trials[38][3],
            option5: trial_list.trials[38][4],
            option6: trial_list.trials[38][5],
            correct: 'air'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[39][0],
            option2: trial_list.trials[39][1],
            option3: trial_list.trials[39][2],
            option4: trial_list.trials[39][3],
            option5: trial_list.trials[39][4],
            option6: trial_list.trials[39][5],
            correct: 'gun'
        },

        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[40][0],
            option2: trial_list.trials[40][1],
            option3: trial_list.trials[40][2],
            option4: trial_list.trials[40][3],
            option5: trial_list.trials[40][4],
            option6: trial_list.trials[40][5],
            correct: 'guess'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[41][0],
            option2: trial_list.trials[41][1],
            option3: trial_list.trials[41][2],
            option4: trial_list.trials[41][3],
            option5: trial_list.trials[41][4],
            option6: trial_list.trials[41][5],
            correct: 'line'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[42][0],
            option2: trial_list.trials[42][1],
            option3: trial_list.trials[42][2],
            option4: trial_list.trials[42][3],
            option5: trial_list.trials[42][4],
            option6: trial_list.trials[42][5],
            correct: 'times'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[43][0],
            option2: trial_list.trials[43][1],
            option3: trial_list.trials[43][2],
            option4: trial_list.trials[43][3],
            option5: trial_list.trials[43][4],
            option6: trial_list.trials[43][5],
            correct: 'air',
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[44][0],
            option2: trial_list.trials[44][1],
            option3: trial_list.trials[44][2],
            option4: trial_list.trials[44][3],
            option5: trial_list.trials[44][4],
            option6: trial_list.trials[44][5],
            correct: 'point'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[45][0],
            option2: trial_list.trials[45][1],
            option3: trial_list.trials[45][2],
            option4: trial_list.trials[45][3],
            option5: trial_list.trials[45][4],
            option6: trial_list.trials[45][5],
            correct: 'food'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[46][0],
            option2: trial_list.trials[46][1],
            option3: trial_list.trials[46][2],
            option4: trial_list.trials[46][3],
            option5: trial_list.trials[46][4],
            option6: trial_list.trials[46][5],
            correct: 'gun'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[47][0],
            option2: trial_list.trials[47][1],
            option3: trial_list.trials[47][2],
            option4: trial_list.trials[47][3],
            option5: trial_list.trials[47][4],
            option6: trial_list.trials[47][5],
            correct: 'day'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[48][0],
            option2: trial_list.trials[48][1],
            option3: trial_list.trials[48][2],
            option4: trial_list.trials[48][3],
            option5: trial_list.trials[48][4],
            option6: trial_list.trials[48][5],
            correct: 'line'
        },
        {
            question: "Click on the intruder/the odd one out",

            option1: trial_list.trials[49][0],
            option2: trial_list.trials[49][1],
            option3: trial_list.trials[49][2],
            option4: trial_list.trials[49][3],
            option5: trial_list.trials[49][4],
            option6: trial_list.trials[49][5],
            correct: 'article'
        }
    ]
};
