from django.db import models

# Create your models here.
class Finch():
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description

finches = [
    Finch('Twerp', 'Brambling', 'Similar in size and shape to the chaffinch, the male brambling has a black head in summer, and an orange breast with white belly. In flight it shows a long white rump.'),
    Finch('Patriot', 'Bullfinch', 'The male bullfinch is unmistakable with his bright pinkish-red breast and cheeks, grey back, black cap and tail, and bright white rump. The flash of the rump in flight and piping whistled call are usually the first signs of bullfinches being present.'),
    Finch('Bird Person', 'Chaffinch', 'The chaffinch is one of the most widespread and abundant bird in Britian and Ireland. Its patterned plumage helps it to blend in when feeding on the ground and it becomes most obvious when it flies, revealing a flash of white on the wings and white outer tail feathers.'),
    Finch('Rose', 'Common rosefinch', 'Common rosefinches (also known as the scarlet rosefinch) are sparrow-sized birds, mottled brown above with a streaked breast, pale belly and forked tail. Males, older than one year, have scarlet head, breast and rump. Females, juveniles and first year males have streaked brown heads and somewhat resemble small corn buntings.'),
    Finch('Chonker', 'Crossbill', 'The crossbill is a chunky finch with a large head and bill which is crossed over at the tips. This crossed bill is used to extract seeds from conifer cones. They are most often encountered in noisy family groups or larger flocks, usually flying close to treetop height.'),
    Finch('Midas', 'Goldfinch', 'The goldfinch is a highly coloured finch with a bright red face and yellow wing patch. Sociable, often breeding in loose colonies, they have a delightful liquid twittering song and call.')
]