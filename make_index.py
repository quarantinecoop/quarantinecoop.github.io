import csv

def writeline(outfile, text):
	outfile.write(text + '\n')

def write_article(month, day, title, abstract, textfile, outfile, year="2020"):
	writeline(outfile, '<article class="masonry__brick entry format-standard animate-this">')
	writeline(outfile, '<div class="entry__thumb">')
	writeline(outfile, '<a href="' + month + '_' + day + '.html" class="entry__thumb-link">')
	writeline(outfile, '<img src="images/' + month + '_' + day + '_' + '1.jpeg" ')
	writeline(outfile, '</a>')
	writeline(outfile, '</div>')

	writeline(outfile, '<div class="entry__text">')
	writeline(outfile, '<div class="entry__header">')
	writeline(outfile, '<h2 class="entry__title"><a href="' + month + '_' + day + 
						'.html">' + title + '</a></h2>')
	writeline(outfile, '<div class="entry__meta">')
	writeline(outfile, '<span class="entry__meta-date"><a href="' + month + '_' + day + 
						'.html">' + month + ' ' + day + ', ' + year + '</a></span>')
	writeline(outfile, '</div>')
	writeline(outfile, '</div>')
	writeline(outfile, '<div class="entry__excerpt"><p>')
	writeline(outfile, abstract)
	writeline(outfile, '</p></div></div>')        
                        # <div class="entry__text">
                        #     <div class="entry__header">
    
                        #         <h2 class="entry__title"><a href="single-standard.html">Just a Standard Format Post.</a></h2>
                        #         <div class="entry__meta">
                        #             <span class="entry__meta-cat">
                        #                 <a href="category.html">Design</a> 
                        #                 <a href="category.html">Photography</a>
                        #             </span>
                        #             <span class="entry__meta-date">
                        #                 <a href="single-standard.html">Apr 29, 2019</a>
                        #             </span>
                        #         </div>
                                
                        #     </div>
                        #     <div class="entry__excerpt">
                        #         <p>
                        #         Lorem ipsum Sed eiusmod esse aliqua sed incididunt aliqua incididunt mollit id et sit proident dolor nulla sed commodo est ad minim elit reprehenderit nisi officia aute incididunt velit sint in aliqua...
                        #         </p>
                        #     </div>
                        # </div>
        
	writeline(outfile, '</article> <!-- end article -->')


with open('index_test.html', 'w+') as outfile:
	# Make the header!
	with open("header_template.txt") as f:
	    lines = f.readlines()
	    outfile.writelines(lines)
	with open("masonry_start.txt") as f:
	    lines = f.readlines()
	    outfile.writelines(lines)
	# for j in range(10):
	# 	write_article(month="april", day="7", title="test", abstract="big test energy",
	# 					textfile="garbage", outfile=outfile)

	with open("masonry_end.txt") as f:
	    lines = f.readlines()
	    outfile.writelines(lines)
	# Make the footer 
	with open("footer_template.txt") as f:
		lines = f.readlines()
		outfile.writelines(lines)