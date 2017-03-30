# poem_generator

### Run
```python poem.py```

### Code Explanation
There are two kind of poem generator, cut-and-paste and probability-jump

cut-and-paste work by
- searching for poem continuation in base text, by matching last text in current poem with text in base_text (if there are more than one the continuation is picked randomly), then
- add continuation to current poem 
- repeat until desired length of letter has reached
code, with seeder is sun, 500 desired length of letter, continuation length 50, and last text length 1
```
with open("beowulf.txt",'r') as beowulf:
      poem = beowulf.read()
      print(cut_and_paste_poem(poem,"sun",500,50,1))
```

probability-jump work by
- Creating probability table of a word jump to another word (p[word1][word2] is probability of if current word is word1 then next word is word2)
- then generate poem with probability table, by considering current word and pick randomly (based on probability) the next word
code, until desired length of word reached
```
with open("byron-don-juan.txt",'r') as beowulf:
      flatten = lambda l: [item for sublist in l for item in sublist]
      words = flatten([line.strip().split() for line in beowulf])
      prob_table = make2gram_probability(words)
      seq_of_word = generate_poem(prob_table,900)
      continuous_poem = " ".join(seq_of_word)
      formatted_poem = continuous_poem.replace('.','.\n').replace('--','--\n').replace(',',',\n')
      print(formatted_poem)
```

### Output
```
---Cut and Paste method, with Beowulf as base text
sun
was climbing higher. Clansmen hastened
to the higled;
billows welled blood; in the briny hall
her ht; he knew there waited
fight for the fiend in thatches over it. A condemned or
banished man, desped still
through width of the world by wise men all
harassed Hrothgar, what hate he bore him,
what mur warrior leader
lifeless lies, who land and hoarder-weary, warrior-guest
from far, a hall-thane herim foes wrestled.
So well had weened the wisest Sce of "Destiny."

VII

HROTHGAR spake, the Scyldin

---Probability Jump, with byron don juan as base text
and duties Of goodness,
 in a heaven-kissing hill;' And there an old smokers,
 Of night was something of course the wave's high station,
 heaven,
 mankind's,
 my gentler purchaser! the preux Chevalier de la Beauveau,
' whose strings Have something of the sole leaf to kicks,
 according to withstand) Could scarce skimm'd the cup of many a hut on; Expounding and his title,
 got a while,
 the fourth,
 to perceive,
 and destroy His mind Makes us free; Let me to me also hearts,
 if all descriptions from off o'ercrowded with her head,
 And is tamed:- And flew into her aim- his tutors very faults.
 Saloon,
 room,
 but no such a yawn,
 or harpsichords,
 Theology,
 fine China cups,
 came and always so great occasions,
 such things upon her lips were to run glibber Than many a sort of pain to the tailor's),
 his senses,
 and has a thing Whose statues warm youth Whom I feel that no doubt,
 if your life,
 for this a year to mix some old black eunuch Castlereagh? The supplicator being new: Nought against actual and o'er it her,
 because his front,
 like watches.
 There was not apt to come again,
' And then their efforts for a marsh so by a dancer,
 much duty; For I am learning to summer dust; and not change its beginning of as far Than could rip: The man to vaunt,
 Not speechless,
 though short the seraglio,
 where lie beneath,
 or far,
 Till some nations freed,
 and lectures he seem'd to the muses Have not in any vanity.
 The supper too much; For woman's tale.
 Thus on their trust; Taught to decide: Emperors are eligible,
 Unless,
 like an existence Before Don Juan,
 and soul,
 his hide,
 Which some skill Smooth'd even when there intervene Pressure of the first a Georgian,
 white walls were never reckon'd; And put on the sick of late: And pride of splendour,
 and sweet,
 He abideth night which Prometheus filch'd for blow,
 Than your good intent was the view of mothers,
 and keep aloof,
 To aid the heaved breast maternal love.
 Here he leap'd.
 He cannot tune the spray,
 Which still are a year or famine,
 any that 's a beauty and one by storm: no shooting (save Scott) in our errors up too long in the rule,
 but crowned,
 The earth,
 And black eyes beneath its brink,
 And as,
 in Adeline had a private and promises to turn out his eye might choose some side Two things were an active share,
 Must still preserved his age,
 Tall,
 stately,
 form'd a wife done a reminiscence.
 'T is surely fair face,
 Sets up your booty,
 You 've battled either dwelt with an awkward than they might.
 If this did,
 He still less of which of bad; Yet I pass my advice!' O reader! pass This I forget,
 Or thrown Into the suitor,
 Titus the cave their too much.
 Amidst this were so dirty With a sword had an hour I loved well- 'T was eating up shells or some,
 while sleeping.
 For the walls to prayers With the gay world's ways; Yet Julia's eyes; Of the progress than be fair Is pleasant,
 so good),
 'A shot And expell'd the dead,
 If they detest at home,
 and fruit,
 to architecture wholly; We tease Her hair,
 And night was left to careen; So gentle,
 charming,
 chaste,
 and now her air,
 Exposed to run,
 The Moslem,
 but Baba spoke of blunt compassion grew sick: The paper With this comparison,
 Where ships sent off his throne,
 Which prove reluctant,
 and the whole.
 The present culprit was broad,
 bright,
 downcast,
 yet new! Oh Love! what is to the stones still have not his hall at a bon-mot head have kept good water Upon the first inclined To hinder Himself from you an exquisite small gear to make us extremely vicious; The love to view.
 They placed in state,
 though I shall sink his grand long married,
 but no rents at least to bind.
 Fill high classes.
 I protest Against a figure gleam'd; Then their hearts abhor- In lieu of a bullfinch,
 and victory were much better in another; The men of late.
 Then sees another line: For I can't find the women up,
 and roast-meats,
 and my advice!' O Wilberforce! thou man had dwelt,
 There was not know; Perhaps his stubble screen.
 But with her fall: they meant For there the uninitiated.
 Alas! by young strangers in lust makes warriors tough)- They are a theme just clearing air.
 'T is giving; All these machines,
 By which 't were plighted Their best it was,
 and like phosphorus on wire,
 And the greater need no explosion cry aloud for you,
 if there was never can summon December's drowsy day When Juan look'd below each further power,
 and preparation Was one to emerge From heart had been awoke with his tutor,
 the time may both oh! ye great friend or even the Venetian Fazzioli.
 But she 'll not for a wicked man grumble when running on his tongue and remarried (this peril past) To lose much better,
 But doubtless to shine,
 Deck'd by and mirk The moment after dinner; But,
 ere the street,
 and hale,
 With martial stoicism,
 nought left his soul of her bright skin For health but adulteration.
 'Ye gods,
 I own plight,
 And iron door,
 which he writhed his way,
 Boded no further downward,
 tall beyond all into arithmetic.
 But I read your fading twilight hour to```
