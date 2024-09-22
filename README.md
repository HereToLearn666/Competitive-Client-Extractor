Introduction:
Some companies host some type of property for their clients on their own websites. In this example, I use Greenhouse, an applicant tracking software company. One of their services includes hosting a listing of the open role at their client's company. People can apply to the job through Greenhouse's website. 

Opportunity:
Because Greenhouse hosts their clients' open roles on the Greenhouse website, it's possible to use an advanced Google search to bring up URLs with the names of their clients in them.

Problem:
The problem is that manually copying each URL would take a while.

Solution:
I wrote a python program that uses BeautifulSoup and csv file writing to extract the client names from the URLs hosted by Greenhouse. It's currently set to do this for the first 30 pages of the Google search. This can be set to any amount of pages.

With minor tweaks based on the URL construction, I have successfully adapted this to be able to create client lists for other applicant tracking software as well.

How Can This Be Used:
This could be adapted for certain lead gen companies. Another use case besides HR software I have come across is higher education. Sometimes there will be a marketing agency or an online course provider that will host lead gen forms on their website for high education institutions. This program could be used to find a list of their clients.
