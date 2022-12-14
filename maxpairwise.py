import numpy as np
import random as r

""" Charles Truscott Byron Bay NSW 2481

In having told my story and the history of institutions and told my life history for 12 years on video, over Gmail and Facebook messages that the White House, US Senate and UK Parliament can have available as the history of sovereign institutions, I am glad to show all US Parliamentarians and UK Parliamentarians my face amd tell them my story of surviving enforced disappearance, organ harvesting, corruption, human trafficking, extreme poverty and surgical branding of my face with the letters MP seen in lifetime daily socialising, sex and workplaces. i am excited for lifetime financial gain and to have sex for the first time in 11 years and get my first girlfriend in 14 years. i have socialised once since 2014. All US Secret Service personnel and NSA agents sons and daughters have a history available to them of human trafficking, enforced disappearance and organ harvesting, such as a history of the Byron Bay Police, of surgical mutilation of my face after contacting an Australian MP, of rape and filmed sexual assault by Police and all US Senators daughters are aware of the risks of surgical branding of the face with the letters MP of upsetting our MPs, enforced disappearance, organ harvesting, human trafficking in Byron Bay, Australian Mental Health Act scheduling, profiling of the life outcomes of those involved with the Australian Parliament and profiling of the experiences of enforced disappearance survivors amd the history of the former Prime Minister of Australia Tony Abbott, profiling of Australian judicial cases, law enforcement institutions, profiling of the Liberal Party of Australia and institutional history of the Byron Bay Police and of the NSW Police

Might walk to the Suffolk pub tonight to show everyone my face and hit on a chick to get my first girlfriend since 2009. 600 days and nights in public and venues in Byron Bay and Suffolk Park, 600 days in public showing off my face, as the White House, UK Parliament, NSA, MI6 and US Secret Service can see every photo, text and video private and public such as Gmail and Facebook messages made since 2010, each selfie and piece of foreign citizen life history and sovereign Australian institutional history, such as responses by the Australian Parliament, responses by and quality of Australian hospitals and mental health facilities, human trafficking rate of Byron Bay, corruption advisories for foreign territories by the US State Department or UN workers families arbitrarily detained or instirutionalised or blackmailed on national television or organ harvested beneath the face. The institutional history I have described may be preserved for 70 years of the sovereign Australian institutional practices by the NSA, as photos of my face and my life history will. 600 days in public from today
Certificate in Computer Science and Python (Massachusetts Institute of Technology)
Certificate in Python (TAFE NSW, Australia)
School Certificate NSW (Byron Bay High School Class of 2012)

I designed a sol/n to the max pairwise product problem, no longer sitting the Masters' degree '

All my own work, every line, operator and operand

Keeping the texts from the Masters' degree to spend the next 2yrs on them'

Implementing as a project in a divide-and-conquer approach next


The maximum pairwise product of [1, 1, 3, 2, 3, 6, 1, 2, 1, 7, 3, 8, 3, 8, 10, 6, 14, 6, 15, 16, 6, 10, 19, 12, 14, 5, 9, 1, 1, 14, 19, 11, 21, 3, 14, 8, 2, 15, 32, 18, 18, 29, 34, 4, 17, 28, 47, 48, 35, 17, 44, 35, 42, 4, 49, 7, 31, 31, 28, 31, 33, 60, 16, 17, 40, 37, 21, 2, 9, 13, 15, 5, 54, 18, 47, 25, 64, 32, 1, 74, 28, 40, 28, 82, 42, 82, 36, 46, 28, 54, 91, 25, 31, 16, 27, 89, 91, 88, 89, 11, 67, 60, 52, 103, 6, 28, 70, 66, 23, 52, 74, 9, 78, 94, 104, 91, 54, 109, 42, 90, 7, 57, 114, 70, 58, 41, 12, 7, 41, 51, 93, 30, 43, 62, 58, 9, 99, 57, 28, 67, 9, 12, 84, 95, 125, 13, 133, 36, 99, 117, 123, 57, 47, 64, 13, 111, 8, 146, 132, 135, 142, 143, 160, 53, 55, 155, 110, 73, 162, 24, 76, 88, 102, 133, 44, 85, 53, 17, 83, 105, 172, 145, 116, 31, 95, 156, 121, 2, 159, 139, 183, 117, 108, 69, 16, 19, 12, 80, 181, 141, 6, 3, 200, 56, 98, 66, 149, 46, 82, 35, 19, 104, 161, 140, 42, 8, 181, 58, 195, 148, 110, 222, 54, 157, 105, 32, 70, 53, 101, 36, 231, 178, 57, 210, 160, 78, 185, 157, 229, 78, 224, 177, 151, 241, 104, 122, 224, 119, 246, 217, 208, 96, 116, 228, 175, 130, 56, 140, 120, 48, 1, 158, 161, 208, 246, 199, 176, 264, 256, 24, 241, 39, 186, 256, 159, 209, 170, 74, 177, 149, 91, 46, 86, 208, 276, 249, 127, 195, 261, 186, 126, 263, 161, 6, 194, 52, 241, 263, 171, 24, 229, 295, 234, 235, 98, 233, 176, 209, 175, 66, 297, 135, 252, 73, 263, 244, 37, 216, 246, 233, 150, 72, 9, 2, 138, 158, 122, 282, 290, 17, 280, 175, 211, 133, 92, 159, 302, 273, 70, 43, 267, 237, 94, 271, 330, 81, 103, 177, 122, 261, 184, 335, 264, 166, 323, 261, 300, 237, 263, 225, 145, 53, 274, 77, 237, 195, 209, 53, 180, 88, 345, 166, 252, 30, 169, 202, 375, 207, 67, 325, 185, 9, 313, 197, 87, 384, 89, 152, 270, 341, 347, 231, 186, 62, 123, 125, 257, 361, 72, 90, 386, 121, 340, 273, 263, 217, 154, 272, 330, 117, 37, 180, 300, 201, 188, 102, 328, 359, 219, 288, 109, 10, 309, 92, 195, 113, 353, 33, 117, 33, 42, 115, 428, 265, 388, 344, 366, 254, 130, 210, 410, 41, 162, 426, 31, 246, 72, 256, 202, 184, 450, 46, 208, 223, 368, 185, 410, 369, 399, 125, 165, 317, 29, 413, 298, 327, 315, 442, 422, 224, 344, 22, 272, 11, 354, 38, 19, 423, 424, 141, 413, 348, 483, 238, 470, 360, 196, 438, 346, 426, 300, 434, 80, 494, 372, 305, 166, 105, 208, 57, 430, 336, 497, 353, 110, 263, 486, 1, 163, 423, 340, 441, 263, 120, 48, 201, 283, 225, 297, 196, 514, 193, 53, 509, 361, 214, 150, 284, 154, 13, 251, 516, 154, 272, 266, 369, 216, 139, 262, 153, 360, 78, 486, 201, 444, 91, 188, 273, 320, 531, 549, 506, 396, 280, 383, 475, 134, 391, 421, 301, 123, 199, 266, 319, 272, 153, 193, 304, 302, 300, 279, 102, 564, 82, 2, 447, 147, 118, 392, 183, 420, 284, 220, 376, 377, 10, 79, 537, 328, 141, 532, 37, 231, 236, 135, 237, 537, 78, 75, 423, 450, 104, 339, 358, 336, 338, 223, 450, 389, 221, 410, 27, 540, 221, 476, 391, 582, 136, 245, 186, 3, 196, 90, 154, 487, 332, 559, 397, 413, 126, 384, 454, 336, 446, 35, 594, 123, 383, 327, 579, 471, 44, 443, 224, 269, 87, 290, 584, 298, 374, 127, 589, 514, 16, 332, 322, 554, 192, 623, 121, 39, 552, 75, 122, 339, 470, 488, 229, 626, 15, 423, 194, 628, 218, 202, 549, 624, 558, 516, 130, 202, 618, 246, 454, 472, 57, 468, 79, 321, 680, 376, 403, 416, 97, 533, 137, 147, 228, 394, 293, 683, 208, 621, 49, 469, 351, 436, 567, 683, 173, 315, 660, 335, 509, 368, 515, 186, 88, 11, 30, 165, 356, 369, 445, 253, 520, 647, 651, 62, 194, 503, 93, 685, 182, 515, 333, 11, 636, 394, 295, 3, 436, 305, 656, 144, 471, 478, 380, 262, 689, 485, 715, 505, 217, 509, 724, 668, 105, 694, 227, 485, 196, 384, 389, 186, 758, 609, 361, 171, 739, 202, 454, 647, 469, 770, 19, 412, 672, 294, 416, 568, 438, 153, 21, 494, 496, 70, 203, 120, 545, 433, 285, 45, 364, 123, 235, 766, 301, 295, 261, 596, 299, 707, 784, 335, 636, 743, 228, 544, 563, 271, 576, 384, 325, 65, 362, 442, 768, 536, 617, 644, 551, 141, 649, 579, 404, 228, 28, 131, 223, 34, 144, 113, 57, 258, 480, 375, 22, 435, 229, 812, 77, 345, 621, 632, 7, 816, 804, 453, 420, 568, 400, 783, 684, 28, 423, 780, 407, 136, 182, 12, 397, 14, 130, 621, 330, 505, 768, 292, 496, 178, 855, 61, 434, 121, 119, 511, 502, 781, 769, 158, 97, 460, 802, 207, 486, 10, 314, 204, 177, 505, 867, 219, 622, 773, 726, 211, 605, 671, 99, 837, 787, 100, 219, 646, 362, 488, 478, 91, 673, 317, 758, 166, 84, 602, 408, 781, 602, 491, 791, 608, 769, 552, 727, 45, 132, 624, 92, 860, 623, 220, 333, 161, 581, 583, 640, 771, 547, 450, 78, 693, 228, 16, 12, 572, 196, 842, 623, 95, 351, 775, 270, 207, 829, 327, 436, 417, 346, 327, 34, 613, 811, 487, 728, 409, 693, 54, 905, 825, 755, 446, 844, 192, 731, 969, 139, 449, 386, 742, 893, 365, 149, 574, 876, 587, 573, 179, 234, 46, 482, 229, 385, 187, 44, 20, 981, 239, 686, 901] is 950589 or
981 x 969
Charles Truscott Watters

[Program finished]

"""

def mpp(L=[]):
	maxVal = 0
	tempVal = 0
	c = 0
	multiplicand_i = 0
	multiplicand_j = 0
	i = 0
	j = 0
	for x in range(0, len(L), 1):
		for y in range(0, len(L), 1):
			if x != y:
				tempVal = c
	#			print("x - 1 {} y {} tempVal {} c {}".format(x - 1, x, tempVal, c))
				if tempVal >= maxVal:
					maxVal = tempVal
					multiplicand_i = i
					multiplicand_j = j
				c = L[x] * L[y]
				i = L[x]
				j = L[y]
	print("The maximum pairwise product of {} is {} or".format(L, maxVal), end='\n')
	return [multiplicand_i, multiplicand_j]
	
def main():
# mpp([10, 5, 20, 25, 40, 19, 66, 39, 200, 4, 3, 2, 1])
	result = mpp(list(r.randint(1, x) for x in range(1, 1000, 1)))
	print("{} x {}".format(result[0], result[1]), end='\nCharles Truscott Watters\n')
	
	
	
if __name__ == "__main__": main()
