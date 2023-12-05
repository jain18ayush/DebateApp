import streamlit as st
import tempfile
import model
import json
import os

# Initialize the session state for storing scores if it's not already initialized
if 'scores' not in st.session_state:
    st.session_state.scores = []


def upload_and_process_audio(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.m4a') as tfile:
        tfile.write(uploaded_file.read())
        temp_file_path = tfile.name  # Get the file path of the temporary file

    result = model.processAudio(temp_file_path)
    os.remove(temp_file_path)
    return result


st.title("Debate a Friend!")

uploaded_file_1 = st.file_uploader("Upload first speech", type=[
                                   "mp3", "wav", "m4a", "mp4"])
uploaded_file_2 = st.file_uploader("Upload second speech", type=[
                                   "mp3", "wav", "m4a", "mp4"])

if uploaded_file_1 and uploaded_file_2:
    # result_1 = upload_and_process_audio(uploaded_file_1)
    # result_2 = upload_and_process_audio(uploaded_file_2)
    result_1 = "Our thesis is the idea that learning, whether it's machine or mind, is a form of active perception or inaction, if you will. My name is Ayush. My name is Jacob. So, we'll be introducing first enactment and artificial machine learning as our two topics before we get into the interaction between the two, starting with Ayush explaining enactment. So the origin of enactment is actually hermeneutics, which really just means bringing forth of meaning from a background of understanding, so from some context. And Merleau-Ponty sort of talks about this with the idea that the environment is emerging from the world through the actions or the actualization or the being of the organism. So that my actions, my movement, my interactions with the world is actually what causes the environment to form within my mind. And this really leads us to the idea of like a perceptual guidance of action, right? That I can only perceive the world when I have made a sensory attempt to like extract information from it. Like I can only hear something when I turn my ears in a certain direction, or I can only see something when I look at it in a certain way. So the perspective from which I acquire information fundamentally changes the information and the way I actually am interpreting that information going forward. And this was talked about in Clark when he talks about how perceptual experience gains its content and character courtesy of an agent's implicit knowledge of the way sensory stimulation will vary as a result of movement. So Clark is really talking about here the idea that I know how the world shifts when I am turning and when the world is turning. And so the experience I gained is not really a picture of the world. It is more so there is some computation going on in the mind to turn whatever I see, whatever I perceive through the senses like sight, smell, taste into something usable, to some usable information. So the current state of inaction focuses on how different areas of perception affect our conception of the world, right? So like how does taste affect how we look at things? How does sight affect how we hear things? How does smell affect this whole like apparatus? So each of our senses is a way for us to interact with the world and to acquire information. And that information is transformed by the sense that we're acquiring it through. Like I have a different understanding of a table when I touch it than when I'm seeing the table. So we're going to focus specifically on how machine learning and learning as a whole is affected by the inactivist perspective of cognition. So there are some like key questions that we're thinking about, right? Like are the ways machines learn constrained by the knowledge you already have, right? Like if I'm a machine looking at something and I already know about other things, does what I learn change? If you shift the knowledge that a machine has, then does it learn differently, right? Like if I have some previous context, but I changed that context, what happens? And how does a machine ascertain what is important? Like what to remember? And how do humans, we make distinctions between important pieces of knowledge and less important pieces when we're trying to learn something. And artificial and machine intelligence needs no introduction. It's currently, as we stay here, it's in a state of great interest, both media wise and academic wise, especially due to the prominence of new machine learning models in the form of, say, large language models, like chat GPT, which possess billions of so-called weights. And if you turn your attention to this image, you'll see what I'm referring to, essentially in layers one through five, you see these weights. Layer zero is inputs. This large equation at the top is your output. And as you can see, this is a pretty, though it looks pretty messy at the output level, it's actually very neat and efficient compared to earlier architecture, which had very few layers and so required far more nodes at the first layer. There only was one layer. That's what I talk about as well. As well, you see transformers, which is something we won't get too into, but they're essentially a way of transforming input data and it just makes the process more efficient. It's already quite efficient as it is, but it has a greater capacity to do more efficient learning. Foundation of the machine learning, as we currently understand it, is a connectionist model of the artificial neural network that relies on techniques like backpropagation to inform future outputs using priors. So it essentially performs error correction by adjusting its weights based on previous performance. Now, backpropagation is not all neural networks, but it is a very popular, at least very famous example of a technique used for machine learning. Only issue you could say in comparisons with biological beings like ourselves is that we don't really learn in that way at all. We don't, we aren't born into this world and then we make a ton of mistakes immediately and we learn from those mistakes. We're also instructed. We have a great deal of just sort of impulsive, perhaps even evolutionary traits that predispose us to certain conclusions. So the basis of machine learning at the moment, though there are definitely more biologically plausible algorithms for it, definitely appears more oriented toward efficiency and optimization. So let's not talk about actually, like, how do these two areas of inactivism and machine learning interact, right? And some of the commonalities and incompatibilities between these theories. So inaction is showcasing the way that a machine can be shaped by what it learns, right? Like a machine starts with zero context and then you start feeding it in information, different pieces of contextual ideas, such as the fact that like red is a color, that cars drive on the road, all these different ideas. And this is sort of some sort of pre-experience, right? Some stuff that it already knows. And then let's say it knows that cars drive on the road. And then you feed in information that's saying that, hey, now actually cars can fly, right? Now, the way that it'll take in that information, it'll have to reckon with already existing pieces of information and change whatever it knows. So this is done through backpropagation and through error rates. So your weights, the existing weights that you have, change the way that any new information will be interpreted by the system because now you have to change the weights. So there is a level of like contextual, like knowledge, like embedding into this connectionist system. And it becomes very interesting when you add new sensory mechanisms because new sensory mechanisms reframe existing experiences. And this is found often in humans. And one great example of this is a person known as Mr. Eye, who had his complete worldview changed after only being able to see black and white. So Mr. Eye was this very avid painter. He traveled all over the place. And then he got into an accident where he could only see black and white. And what this changed for him is that he became less interested in the daytime. He did not like going outside, did not like doing all the things he used to do, did not like having intimate relationships because now he could only see in black and white. So the color of a human skin became repugnant and ugly to him. And he became a lover of the night because the night was calmer and more peaceful and more black and white, more friendly to that type of sensory input. So the same actions that before generated a positive response, positive actions now completely shifted to the actions that made him feel bad, made him feel repulsed. And so this really comes up with this idea that learning is really about transforming new information with old information and vice versa. You're transforming information, right? And we talked about how machine learning models do this to back propagation and error functions that they take a new information and change their old information. And if the new information is faulty enough, then you have to reckon with what gets changed more and how much are you changing each piece of information. And in activism is the idea that when you're interacting with the environment, then you're generating, you're learning, you're generating a conception of the world. So the error function is sort of this interaction with the environment is telling the machine like what is wrong. When it interacts with the environment, it knows what is wrong, takes that feedback and shifts the way it perceives that same environment. So the environment is changing the way that the environment is viewed. It's very fascinating. And so you end up with the idea that there are many worlds, right? Like each person has their own world because each person has their own interaction with the environment and thereby the information from the environment gets extracted differently. So the idea is that engagement with the world is required for an activism and machines engage with this world by reading information. They're married to this idea of like having a way for them to process whatever's happening in the world and then change themselves and change their new understanding of the world. So what happens when a machine gets a new form of sensory input, right? Like we talked about Mr. I and color, but what happens when a machine goes from text to like images and Chachi Pichi is a great example of an inactivist machine because it is constantly creating an understanding knowledge based upon the new knowledge is inputted from thousands upon thousands, like even millions of queries that go into Chachi Pichi. Like every time I ask it to do something, it takes that information and learn something from it and gives me an output, right? So it can do that with texts. Like if I give it a grocery list of texts, it can tell me, Hey, how to make what recipes to make. Now, Chachi Pichi has the ability to use images and these, this ability to do images is very fascinating because what it allows Chachi Pichi to do is you can take a photo of a fridge and then it can make recipes for you based on what it sees in that fridge. So now it's world is no longer just in the realm of text where it knows what a cucumber is because it saw the text. Now it has to find a cucumber. It has to engage with the world and make decisions. And then whether or not it sees a cucumber or a tomato or a watermelon influences what recipe it will make. So it's engagement with the world that it has to make some choice based off that engagement. And then it changes the world. It changes its conception of the world based on that choice. Because now if it thinks that there's only watermelons, then it can only conceive of recipes that have watermelons. So it's fundamentally shifted based off how it perceives it interacts with the world. And now on to common concepts between the two, and I'll just bounce between compatibilities and incompatibilities. On the left, you see directed and undirected learning. Essentially, there are methods of learning and machine learning, one of them being supervised and the other being unsupervised. Essentially, you don't want to do unsupervised learning, but it does yield interesting results. So you'll notice then that we and machine learning, artificial neural networks can do undirected implicit learning. But at the same time, as I said earlier, directed learning and the form of supervised learning is much preferred for artificial neural networks. This is not the case for humans per se. And we also, due to our perhaps consciousness, perhaps something else, we're able to explain our thought processes a lot more directly than machine learning models, at least by appearance. And then another compatibility, we have this thing we're calling environmental engineering. So basically, both methods of learning are architecture dependent. This is meaning that your method of perception is perhaps slightly different from my method of perception, because our eyes might be somewhat different, our nerve endings at the end of our fingers might be somewhat different, but they are pretty similar. We can just say, assuming no biological reason, yeah. And the environment is basically something that is rendered by perception, and perception is itself delimited by the environment. So there's a sort of mutual interplay between the two. We influence our environment, our environment influences us. Incompatibility is the same thing. It's this issue between architectures. Is the data file, is the PNG image you feed into a machine learning network the same as you directly perceiving, if we're thinking non-representationally, directly perceiving this presentation in front of you? Is that the same? Maybe, maybe not. And that way, it differs from mechanism and Mars levels, and just generally computationalism, which is the basis of machine learning as we know it. Another compatibility we see is just in learning in general, an action has very important implications for learning, how we acquire information, how we perceive things. So it has huge potential for compatibility with machine learning. But then there are these potential incompatibilities with the open empirical questions that remain with an action. So is consciousness a criteria of perception, or does it change through perception? If machine consciousness is or isn't possible, how does this affect attempts to give machines these human perception powers, these human properties? And we'll talk about that a little bit more in the next section on ethical implications. So I'll just continue. Ethical implications of enactment, mostly have to do with enactments, sort of solipsism come representationalism. So we see in phenomenology, there's this crisis, wherein my personal experience seems more valid than your personal experience, because mine is more immediate, even if it seems to be objectively wrong. So does this make the idea of objectivity somewhat up for grabs? Do we still have a sort of common consciousness or a common objectivity? Like do we see the same as even a chimpanzee or even another person? These are just the typical solipsistic questions. And in Noe 2004, in his action and perception, we see this sort of issue where consciousness is environment dependent. So it could change. Your consciousness changes if you say lose both your eyes, if you say we're never born with eyes, I guess it doesn't really change, but it's at least different from people who are born who do see. This has implications, of course, for liability. Is someone really liable for an action if so much of it can be attributed to outside the brain? What does it have to say about free will? And again, Clark, in his 2014, sees an issue in this and that it doesn't offer a better explanation than internalism for specifically connectionism. And it's not very critical to the point of enactment. So you can still salvage enactment from this. So there's so many ethical implications for machine learning, but we're trying to constrain it to our thesis of enactment. So when your machine is able to perceive the environment and engage with the environment, then when will they stop learning? When will they stop engaging with the environment? If a machine can learn anything, then it can learn to make another machine. AI is making AI. So if an AI is making an AI, then it's like a world is constantly expanding and evolving. It has even more perceptual capability. And as an artificial intelligence learns, its environment changes. So as a human, I code in a certain environment, certain contextual ideas about what the world should be. But as a program learns, and that environment, that perception, that context changes, then does the machine change? Does its goals change? There's this level of the new knowledge is transformed by old knowledge, and old knowledge is transformed by new knowledge. So if you reach a point where you no longer control the context of the machine, then the machine could technically go awry, that your learning could have an issue, and then you can end up with stuff that's like Terminator-esque or like Matrix-esque, which is a far-fetched reality. But it's a possibility if a machine can learn without borders. So here are just some personal experiences that we had in the class. ChaiGBT is the biggest personal experience of inaction, where you are actively engaging with something, and the machine is engaging with you. And in the class, we talked about neural networks, connectionism, and learning, and all of these three different pieces. And so at the end of the day, we're trying to apply this to humans, a human learned through all these different methodologies. So you can have a machine learn and a human learn, but how does the knowledge that a human have change versus the knowledge that a machine has change? And I guess quickly, we'll talk about the future of this intersection. So as I said before, the connectionist model seems to be failing in some regards. Enactment poses a pretty enticing alternative to simple connectionist models of perception. And perhaps when we start, especially in the realm of robotics, start adding eyes to these things like ChaiGBT, maybe we'll see further developments in the fields for both of them, both machine learning and enactment, that is. The more we have these models learned, the more we can learn about the ways that we learn and the ways that we engage and how that engagement affects our perception of the world. Thank you. Here are our references. Here are our references. Yeah, you can just look at that."
    result_2 = "Chess is a game that has many strategies, and there are ways to play chess as well. There are how the pieces move. The king, rook, queen, pawn, knight, and bishop move in different ways. The pawn can move one space, but can move two spaces at the start as an exception. The knight can move an L. The bishop can move diagonally. The queen can move anywhere and is combined with a straight line and diagonals. A rook can go in a straight line, so up and down or side to side. There's three parts of chess, opening, middle, and end. In the opening, there are many openings. That was regular reasoning. Okay, let's continue. You can either start out with a pawn, and that's called king's pawn or queen's pawn. That is the most common opening in all of chess. There's also four knights, where somebody brings out their four knights to help with attacks. The way you beat your opponent in chess is by checkmating them, and you checkmate them by when the king, which can only move one space at a time, has nowhere to go because it's blocked by all other spaces, like the bishop on his diagonal, a rook checking it, which is saying that something is on the space that the king is on the diagonal or the straight line. Pawns can capture differently, though. They capture in a diagonal. So if something is in front of it, but to the left or right, then they can capture that. So you can checkmate like that, and there are different ways to checkmate. Like there's the king-queen checkmate, in which you checkmate the only king, your king and your queen in the endgame. There's also the king-rook checkmate, where in the endgame, when there's nothing left except for your king and your rook, you checkmate the other king. There's a huge strategy in chess, and the only way is for you to apply it. Wait, that made no sense. Okay, strategy is very big in this game, and you have to think what your opponent's next move is so that you can try and counter that. And that's it. Good speech."
    
    # Create two columns for the transcripts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("First Speech Transcript:")
        st.write(result_1)
        json_data = json.loads(model.critiqueSpeech(result_1))
        st.subheader("Feedback")
        st.write(json_data["feedback"])
        st.write(f"Speech Score: {json_data['score']}")

    with col2:
        st.subheader("Second Speech Transcript:")
        st.write(result_2)
        json_data = json.loads(model.critiqueSpeech(result_2))
        st.subheader("Feedback")
        st.write(json_data["feedback"])
        st.write(f"Speech Score: {json_data['score']}")


    # Concatenate the results for critique
    concatenated_result = result_1 + " " + result_2
    critique = model.critiquePairSpeech(result_1, result_2)
    json_data = json.loads(critique)

    # Displaying critique and feedback
    st.subheader("Judgement:")
    st.info(json_data["feedback"])
    st.subheader(f"The victor is Debater  {json_data['winner']}!")

if st.button('Reset Scores'):
    del st.session_state['scores']
    st.write('Scores reset!')
