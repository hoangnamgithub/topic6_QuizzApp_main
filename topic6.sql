-- database selection
use master
use QuestionBank

-- Version, Server check
SELECT @@SERVERNAME
SELECT @@VERSION

-- Describe table
EXEC sp_help 'questions'
EXEC sp_help 'userResult'
EXEC sp_help 'resultsDetail'
SELECT * FROM questions
SELECT * FROM userResult
SELECT * FROM resultsDetail

-- Drop everything
DROP DATABASE QuestionBank
DROP TABLE questions
DROP TABLE userResult
DROP TABLE resultsDetail

-- Delete data
DELETE FROM questions
DELETE FROM userResult
DELETE FROM resultsDetail

-- Data for fast insertion
INSERT INTO questions (quesID, Question, AnswerA, AnswerB, AnswerC, AnswerD, CorrectAnswer) VALUES
    ('Q01', 'Find the word with different pronunciation []:', 'A. march[ed]', 'B. leak[ed]', 'C. act[ed]', 'D. leap[ed]', 'C'),
    ('Q02', 'Find the word with different pronunciation []:', 'A. br[a]ke', 'B. j[a]m', 'C. ch[a]se', 'D. sn[a]ke', 'B'),
    ('Q03', 'Find the word with different pronunciation []:', 'A. walk[ed]', 'B. talk[ed]', 'C. work[ed]', 'D. look[ed]', 'D'),
    ('Q04', 'Find the word with different pronunciation []:', 'A. play[ed]', 'B. stay[ed]', 'C. say[ed]', 'D. lay[ed]', 'D'),
    ('Q05', 'Find the word with different stress:', 'A. photograph', 'B. photographer', 'C. photographic', 'D. photography', 'D'),
    ('Q06', 'Find the word with different stress:', 'A. economy', 'B. economic', 'C. economist', 'D. economical', 'D'),
    ('Q07', 'I believe that tennis is one of the most challenging sports, _______ ?', 'A. dont I', 'B. is it', 'C. isnt it', 'D. do I', 'C'),
    ('Q08', 'The older generations find modern art completely _______ .', 'A. impenetrable', 'B. pre-eminent', 'C. impassable', 'D. inveterate', 'A'),
    ('Q09', 'The director gave her a(n) _______ hat.', 'A. attractive blue silk', 'B. silk blue attractive', 'C. attractive silk blue', 'D. blue silk attractive', 'A'),
    ('Q10', 'The famous basketball pro joked that he was over the _______ and it was time for him to retire.', 'A. mountain', 'B. cliff', 'C. hill', 'D. valley', 'C'),
    ('Q11', 'After my younger brother had moved to Los Angeles, his room got _______ .', 'A. the messiest', 'B. more and more messy', 'C. the messier and the messier', 'D. messier and messier', 'D'),
    ('Q12', 'The recently retired footballer _______ his locker and sadly left the stadium.', 'A. held out', 'B. put off', 'C. cleared out', 'D. made up', 'C'),
    ('Q13', 'The most important choice to make to ensure _______ when swimming is that of your equipment.', 'A. safely', 'B. safety', 'C. safe', 'D. safer', 'B'),
    ('Q14', 'It sounded like a pipe dream, but he was so enthusiastic it was hard not to get excited ______ him.', 'A. for', 'B. with', 'C. about', 'D. in', 'A'),
    ('Q15', 'Some countries are still lagging behind the rest of the world in the vaccine race _______ a large number of resources diverted to advertising campaigns.', 'A. although', 'B. because', 'C. due to', 'D. despite', 'D'),
    ('Q16', 'My parents took me on lots of trips when I was a child, and I _______ the love of travelling.', 'A. never lost', 'B. have never lost', 'C. had never lost', 'D. never lose', 'B'),
    ('Q17', '_______ extra buses, they successfully attracted thousands of fans to the concert.', 'A. Put on', 'B. Being putting on', 'C. To put on', 'D. Having put on', 'D'),
    ('Q18', '_______ will they discover any hidden talents they might have.', 'A. Until they start performing', 'B. Only when they start performing', 'C. Hardly had they started performing', 'D. As soon as they started performing', 'B'),
    ('Q19', 'Children and parents should be concerned about _______ knowledge of growing vegetables and raising pets.', 'A. bridging', 'B. taking', 'C. acquiring', 'D. voicing', 'C'),
    ('Q20', 'She _______ by the number of people that came to wish him luck on his new endeavour.', 'A. stunned', 'B. was stunned', 'C. stunning', 'D. to stun', 'B'),
    ('Q21', 'My grandparents _______ about their life are always really interesting.', 'A. summaries', 'B. adaptations', 'C. anecdotes', 'D. variations', 'C'),
    ('Q22', 'Find the CLOSEST word(s) to []: Recent medical research into the new virus has [dispelled] fears that it is usually fatal.', 'A. escalated', 'B. influenced', 'C. removed', 'D. balanced', 'C'),
    ('Q23', 'Find the CLOSEST word(s) to []: Children who know how to [tend] a garden can grow up to be environmentally conscious individuals.', 'A. conduce', 'B. care', 'C. trend', 'D. destroy', 'B'),
    ('Q24', 'Find the OPPOSITE word(s) to []: The government announced [out of the blue] that there would be an investment in tidal energy.', 'A. surprisingly', 'B. calmingly', 'C. continuously', 'D. predictably', 'D'),
    ('Q25', 'Find the OPPOSITE word(s) to []: Hackers are those who make our lives miserable by hacking into computers or spreading [malicious] viruses.', 'A. harmful', 'B. depressing', 'C. safe', 'D. essential', 'C'),
    ('Q26', 'Jonna and David, two education students, are discussing how babies learn. Jonna: “Learning videos can help children learn some basic vocabulary.’ David: ’ _______ . They learn less effectively from screens.‘', 'A. No doubt', 'B. I couldnt agree with you more', 'C. Im afraid youre wrong', 'D. Youre right', 'C'),
    ('Q27', 'John is having dinner at Lindas house. John: “The boiled chicken tastes so good!’ Linda: ’ _______ ‘', 'A. Im glad you like it', 'B. No, dont worry', 'C. I dont, either', 'D. Sure. Id love to', 'A'),
    ('Q28', 'Choose the part that needs correction: After [graduating] from Columbia in 2003, he [becomes] a [scholar], [travelling] to Oxford.', 'A. graduating', 'B. becomes', 'C. scholar', 'D. travelling', 'B'),
    ('Q29', 'Choose the part that needs correction: Jellyfish are not [harmless] since [its] sting can [cause] a serious [allergic] reaction in some people.', 'A. harmless', 'B. its', 'C. cause', 'D. allergic', 'B'),
    ('Q30', 'Choose the part that needs correction: Some people believe animal [behaviour] could offer a [viable] alternative [means] of earthquake [detective].', 'A. behaviour', 'B. viable', 'C. means', 'D. detective', 'D'),
    ('Q31', 'Closest in meaning: Its ten years since I came back to my hometown.', 'A. The last time I came back to my hometown was ten years.', 'B. I havent come back to my hometown for ten years.', 'C. I have come back to my hometown for ten years.', 'D. I last come back to my hometown ten years ago.', 'B'),
    ('Q32', 'Closest in meaning: “Dont put your fingers in your mouth again, Dan.’ said Dans mother to him', 'A. Dans mother reminded him to put his fingers in his mouth again.', 'B. Dans mother told him not to put his fingers in his mouth again.', 'C. Dans mother asked him not to put your fingers in his mouth again.', 'D. Dans mother threatened to put his fingers in his mouth again.', 'B'),
    ('Q33', 'Closest in meaning: It is required by law that those who are in close contact with covid-19 are isolated.', 'A. Those who are in close contact with covid-19 may be isolated.', 'B. Those who are in close contact with covid-19 should be isolated.', 'C. Those who are in close contact with covid-19 will be isolated.', 'D. Those who are in close contact with covid-19 must be isolated.', 'D'),
    ('Q34', 'Choose the best combines: She gave a great performance at the festival. She became more famous.', 'A. Were she not to give a great performance at the festival, she wouldnt become more famous.', 'B. Suppose that she had given a great performance at the festival, she wouldnt have become more famous.', 'C. Had she not given a great performance at the festival, she wouldnt have become more famous.', 'D. If she had given a she wouldnt have become more famous, she would have become more famous.', 'C'),
    ('Q35', 'Choose the best combines: Tim dropped out of school at the age of 14. He regrets it now.', 'A. As long as Tim didnt drop out of school at the age of 14, he wouldnt regret it now.', 'B. Tim wished he hadnt dropped out of school at the age of 14.', 'C. If Tim hadnt dropped out of school at the age of 14, he wouldnt regret it then.', 'D. If only Tim wouldnt drop out of school at the age of 14.', 'B'),
    ('Q36', 'When asked about his plans for the future, he remained _______ and did not reveal much.', 'A. open', 'B. secretive', 'C. indifferent', 'D. generous', 'B'),
    ('Q37', 'Despite _______ to understand the complex theories, she eventually mastered the subject.', 'A. struggling', 'B. struggle', 'C. struggled', 'D. struggles', 'A'),
    ('Q38', 'The committee decided to _______ the proposal due to a lack of supporting evidence.', 'A. accept', 'B. reject', 'C. consider', 'D. review', 'B'),
    ('Q39', 'Find the CLOSEST word(s) to []: The new regulations are designed to [mitigate] the risks associated with the procedure.', 'A. increase', 'B. aggravate', 'C. lessen', 'D. neglect', 'C'),
    ('Q40', 'Find the CLOSEST word(s) to []: After the long and arduous journey, the explorers [reached] the remote village.', 'A. departed', 'B. left', 'C. vacated', 'D. arrived at', 'D'),
    ('Q41', 'Find the OPPOSITE word(s) to []: His [modest] approach to the success was appreciated by everyone.', 'A. humble', 'B. arrogant', 'C. simplistic', 'D. reasonable', 'B'),
    ('Q42', 'Find the OPPOSITE word(s) to []: The results were [ambiguous], leaving room for multiple interpretations.', 'A. vague', 'B. clear', 'C. uncertain', 'D. dubious', 'B'),
    ('Q43', 'Choose the part that needs correction: The committee [has been meeting] every Monday [for the past] three months, [but the final decision] [has yet to] be made.', 'A. has been meeting', 'B. for the past', 'C. but the final decision', 'D. has yet to', 'D'),
    ('Q44', 'Choose the part that needs correction: The [impressionist] paintings [in this exhibit] are [among the most] [beautifully] one has ever seen.', 'A. impressionist', 'B. in this exhibit', 'C. among the most', 'D. beautifully', 'D'),
    ('Q45', 'Choose the part that needs correction: [Neither] of the solutions [offered] were [satisfactory] enough to [solve] the issue.', 'A. Neither', 'B. offered', 'C. were', 'D. solve', 'C'),
    ('Q46', 'Closest in meaning: The team is expected to finalize the project by the end of the month.', 'A. The project was finalized by the end of the month.', 'B. The team is expected that the project is finalized by the end of the month.', 'C. The team should finish the project by the end of the month.', 'D. The team might finalize the project by the end of the month.', 'C'),
    ('Q47', 'Closest in meaning: "I regret not attending the conference last week," he said.', 'A. He said he regrets not attending the conference last week.', 'B. He regretted not attending the conference the previous week.', 'C. He regrets not attending the conference last week.', 'D. He regrets having not attended the conference last week.', 'B'),
    ('Q48', 'Closest in meaning: Its essential that every participant reads the guidelines before joining.', 'A. Every participant should read the guidelines before joining.', 'B. Every participant might read the guidelines before joining.', 'C. Every participant can read the guidelines before joining.', 'D. Every participant will read the guidelines before joining.', 'A'),
    ('Q49', 'Choose the best combines: She finished her homework early. She had more time to relax.', 'A. Had she not finished her homework early, she wouldnt have had more time to relax.', 'B. If she had finished her homework early, she would have had more time to relax.', 'C. She finished her homework early and had more time to relax.', 'D. She wouldnt have had more time to relax if she finished her homework early.', 'A'),
    ('Q50', 'Choose the best combines: Mark forgot to lock the door. The house was burgled.', 'A. If Mark had locked the door, the house wouldnt have been burgled.', 'B. The house was burgled if Mark forgot to lock the door.', 'C. Mark forgot to lock the door because the house was burgled.', 'D. The house was burgled so Mark forgot to lock the door.', 'A'),
    ('Q51', 'The new manager wants to _______ the team to increase productivity.', 'A. demoralize', 'B. motivate', 'C. ignore', 'D. demote', 'B'),
    ('Q52', 'She had a _______ look on her face when she heard the news.', 'A. delighted', 'B. confusing', 'C. confused', 'D. excitement', 'C'),
    ('Q53', 'The _______ to the city was closed due to the heavy snowfall.', 'A. entrance', 'B. access', 'C. exit', 'D. road', 'A'),
    ('Q54', 'His decision was influenced by both logical reasoning and _______.', 'A. emotions', 'B. emotional', 'C. emotive', 'D. emotionality', 'A'),
    ('Q55', '_______ he apologized, she still refused to talk to him.', 'A. Although', 'B. However', 'C. Because', 'D. As', 'A'),
    ('Q56', 'It is crucial that the documents _______ before the deadline.', 'A. is submitted', 'B. are submitted', 'C. were submitted', 'D. have submitted', 'B'),
    ('Q57', 'The artists style is _______ from the traditional forms.', 'A. distinguished', 'B. distinguishing', 'C. distinguishable', 'D. distinguishedly', 'C'),
    ('Q58', 'To prevent errors, you should _______ check your work.', 'A. rarely', 'B. seldom', 'C. thoroughly', 'D. scarcely', 'C'),
    ('Q59', '_______ a good nights sleep, she felt refreshed and ready for the day.', 'A. After having', 'B. Despite', 'C. In spite of', 'D. Because of', 'A'),
    ('Q60', 'The _______ of the meeting was to discuss the upcoming project.', 'A. point', 'B. purpose', 'C. end', 'D. reason', 'B'),
    ('Q61', 'Many people have _______ interests in both science and art.', 'A. diverge', 'B. divergent', 'C. diverged', 'D. diverging', 'B'),
    ('Q62', 'The students _______ was evident in his carefully prepared presentation.', 'A. preparation', 'B. unpreparedness', 'C. confusion', 'D. unprepared', 'A'),
    ('Q63', 'Find the CLOSEST word(s) to []: The new policy will [facilitate] the process of obtaining a visa.', 'A. hinder', 'B. complicate', 'C. ease', 'D. aggravate', 'C'),
    ('Q64', 'Find the CLOSEST word(s) to []: The results [confirmed] the effectiveness of the new treatment.', 'A. disproved', 'B. validated', 'C. questioned', 'D. contradicted', 'B'),
    ('Q65', 'Find the OPPOSITE word(s) to []: His [amiable] nature made him popular among his peers.', 'A. disagreeable', 'B. pleasant', 'C. friendly', 'D. kind', 'A'),
    ('Q66', 'Find the OPPOSITE word(s) to []: The managers [obscure] instructions left everyone confused.', 'A. clear', 'B. vague', 'C. uncertain', 'D. ambiguous', 'A'),
    ('Q67', 'Choose the part that needs correction: The [companys] [success] was [largely] [due to] its innovative marketing strategies.', 'A. companys', 'B. success', 'C. largely', 'D. due to', 'A'),
    ('Q68', 'Choose the part that needs correction: [Each] of the [students] [have] [submitted] their assignments on time.', 'A. Each', 'B. students', 'C. have', 'D. submitted', 'C'),
    ('Q69', 'Choose the part that needs correction: [Despite] the [weather] [was cold], they [decided to] go hiking.', 'A. Despite', 'B. weather', 'C. was cold', 'D. decided to', 'C'),
    ('Q70', 'Choose the part that needs correction: The [committees] [recommendations] were [not] only [accepted], but also implemented immediately.', 'A. committees', 'B. recommendations', 'C. not', 'D. accepted', 'C'),
    ('Q71', 'Closest in meaning: She couldnt help but laugh at the joke.', 'A. She was able to help but laugh at the joke.', 'B. She found the joke laughable.', 'C. She had to laugh at the joke.', 'D. She could help but laugh at the joke.', 'C'),
    ('Q72', 'Closest in meaning: The deadline for the project is approaching fast.', 'A. The project deadline is receding fast.', 'B. The project deadline is moving quickly.', 'C. The project deadline is drawing near.', 'D. The project deadline is distancing.', 'C'),
    ('Q73', 'Closest in meaning: It is important to adhere to the guidelines.', 'A. It is significant to ignore the guidelines.', 'B. It is vital to stick to the guidelines.', 'C. It is necessary to reject the guidelines.', 'D. It is irrelevant to follow the guidelines.', 'B'),
    ('Q74', 'Closest in meaning: I wish I had not made that mistake.', 'A. I wish I made that mistake.', 'B. I regret making that mistake.', 'C. I am happy I made that mistake.', 'D. I wish I make that mistake.', 'B'),
    ('Q75', 'Choose the best combines: He missed the train. He was late for the meeting.', 'A. He was late for the meeting because he missed the train.', 'B. He missed the train because he was late for the meeting.', 'C. He was late for the meeting despite missing the train.', 'D. He missed the train so he was not late for the meeting.', 'A'),
    ('Q76', 'Choose the best combines: She studied hard. She failed the exam.', 'A. She failed the exam so she studied hard.', 'B. Despite studying hard she failed the exam.', 'C. She failed the exam because she studied hard.', 'D. If she had studied hard she would fail the exam.', 'B'),
    ('Q77', 'Choose the best combines: They left early. They avoided the traffic.', 'A. They avoided the traffic by leaving early.', 'B. If they left early they avoided the traffic.', 'C. They avoided the traffic so they left early.', 'D. They left early because they avoided the traffic.', 'A'),
    ('Q78', 'Choose the best combines: He forgot to turn off the lights. The electricity bill was high.', 'A. He forgot to turn off the lights but the electricity bill was high.', 'B. He forgot to turn off the lights so the electricity bill was high.', 'C. The electricity bill was high because he forgot to turn off the lights.', 'D. The electricity bill was high so he forgot to turn off the lights.', 'B'),
    ('Q79', 'Choose the best combines: She did not have the qualifications. She was not hired for the job.', 'A. She was not hired for the job because she did not have the qualifications.', 'B. She did not have the qualifications but she was hired for the job.', 'C. She was hired for the job because she did not have the qualifications.', 'D. She was not hired for the job so she did not have the qualifications.', 'A'),
    ('Q80', 'Choose the best combines: They traveled by car. They enjoyed the scenery.', 'A. They traveled by car and they enjoyed the scenery.', 'B. They enjoyed the scenery so they traveled by car.', 'C. They traveled by car because they enjoyed the scenery.', 'D. They enjoyed the scenery but they traveled by car.', 'A'),
    ('Q81', 'Choose the best combines: The weather was terrible. They decided to go ahead with the picnic.', 'A. The weather was terrible so they decided to go ahead with the picnic.', 'B. Despite the terrible weather they decided to go ahead with the picnic.', 'C. They decided to go ahead with the picnic because the weather was terrible.', 'D. They decided to go ahead with the picnic but the weather was terrible.', 'B'),
    ('Q82', 'Choose the best combines: He was very tired. He continued working.', 'A. Although he was very tired he continued working.', 'B. He continued working but he was very tired.', 'C. He continued working so he was very tired.', 'D. He was very tired and he continued working.', 'A'),
    ('Q83', 'Choose the best combines: She prepared thoroughly. She passed the exam with flying colors.', 'A. She prepared thoroughly so she passed the exam with flying colors.', 'B. She passed the exam with flying colors but she prepared thoroughly.', 'C. She passed the exam with flying colors because she prepared thoroughly.', 'D. She prepared thoroughly and she passed the exam with flying colors.', 'A'),
    ('Q84', 'The _______ of the issue requires immediate attention.', 'A. triviality', 'B. complexity', 'C. simplicity', 'D. unimportance', 'B'),
    ('Q85', 'Her approach to solving the problem was both innovative and _______.', 'A. outdated', 'B. traditional', 'C. effective', 'D. unproductive', 'C'),
    ('Q86', 'The CEOs _______ in handling the crisis was widely praised.', 'A. inexperience', 'B. incompetence', 'C. expertise', 'D. confusion', 'C'),
    ('Q87', 'The _______ of the new law will be reviewed next month.', 'A. implementation', 'B. implement', 'C. implemented', 'D. implements', 'A'),
    ('Q88', '_______ the weather forecast, they decided to postpone the event.', 'A. Despite', 'B. According to', 'C. Due to', 'D. In spite of', 'B'),
    ('Q89', 'Her _______ attitude towards the project made her a valuable team member.', 'A. indifferent', 'B. enthusiastic', 'C. apathetic', 'D. careless', 'B'),
    ('Q90', '_______ they were warned about the risks, they decided to proceed.', 'A. Although', 'B. Despite', 'C. Because', 'D. As', 'A'),
    ('Q91', 'The _______ of his argument was compelling and well-researched.', 'A. ambiguity', 'B. clarity', 'C. confusion', 'D. vagueness', 'B'),
    ('Q92', 'She had a _______ interest in environmental issues.', 'A. mild', 'B. keen', 'C. vague', 'D. distant', 'B'),
    ('Q93', 'The _______ of the new product exceeded all expectations.', 'A. rejection', 'B. failure', 'C. reception', 'D. refusal', 'C'),
    ('Q94', 'Find the CLOSEST word(s) to []: His explanation [clarified] the confusing instructions.', 'A. complicated', 'B. puzzled', 'C. explained', 'D. elucidated', 'D'),
    ('Q95', 'Find the CLOSEST word(s) to []: The new policy aims to [improve] the current system.', 'A. degrade', 'B. enhance', 'C. diminish', 'D. reduce', 'B'),
    ('Q96', 'Find the OPPOSITE word(s) to []: The [reliable] source provided accurate information.', 'A. trustworthy', 'B. unreliable', 'C. accurate', 'D. certain', 'B'),
    ('Q97', 'Find the OPPOSITE word(s) to []: His [meticulous] approach to the task ensured no mistakes were made.', 'A. careless', 'B. careful', 'C. thorough', 'D. detailed', 'A'),
    ('Q98', 'Choose the part that needs correction: The [lecture] was [informative] and [insightful], [provided] a deep understanding of the topic.', 'A. lecture', 'B. informative', 'C. insightful', 'D. provided', 'D'),
    ('Q99', 'Choose the part that needs correction: [While] the [results] were [disappointing] [but] they offered valuable insights.', 'A. While', 'B. results', 'C. disappointing', 'D. but', 'D'),
    ('Q100', 'Choose the part that needs correction: The [policy] was [implemented] [without] [further delay] to ensure compliance.', 'A. policy', 'B. implemented', 'C. without', 'D. further delay', 'A')