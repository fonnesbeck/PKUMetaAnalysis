Dear Dr. Peters,

Thank you for your timely review of our manuscript *Estimating the probability of IQ impairment from blood phenylalanine for phenylketonuria patients: A hierarchical meta-analysis*. We appreciate the feedback from each of the reviewers, and feel that the resulting changes have strengthened our paper. As requested, we have addressed each of the comments in turn, and you will find a list of our responses accompanying this leter. Our responses appear below each of the issues, in distinct formatting so that they may easily be distinguished by you and the reviewers. Please re-evaluate our paper in light of these changes.

Best regards,

Christopher J. Fonnesbeck
<br>Department of Biostatistics
<br>Vanderbilt University School of Medicine
<br>Nashville, TN

---

COMMENTS FOR THE AUTHOR:

Reviewer #1: The manuscript introduces a new and undoubtedly important method into the field of outcome studies of IEM in general and PKU in particular.

In the abstract the authors write "We believe this metric is easily interpretable by clinicians, and hence useful in making recommendations for Phe intake.". Although this statement might be true, this will not hold for understanding of the rationale of the approach and thereby the evaluation of the validity of the conclusions. A simple look-up figure might be too early to serve as a basis for treatment recommendation in PKU. In particular, I am worried that readers just take home the 400 µmol/L result as the main message of the meta-analysis.
Therefore I recommend making some major and some minor revisions before this article can be published in the JIMD.

Major concerns:

An abbreviation list would be very helpful

    This has been added as an appendix.

Does the reader has to take into account BCI values when interpreting the results of the analysis?

    Absolutely, as it is a measure of the uncertainty in the estimation of parameters. However, credible intervals do not apply to the plots in figure 3 because these are tail area probabilities of the posterior predictive distribution (i.e. integrals of the distribution). We have added an explanatory sentence regarding BCI and the integrated probability in the results.

What is the interpretation of the positive additive fixed effect of critical period concurrent Phe? Does this mean effects have to be summed up?

    This means that the effect is additive to the other effects in the model. We have added a sentence in paragraph 5 of the results with an example.

Page 2, line 43: The statement, "In general, the treatment goal is a Phe level below 360 µmol/L" is not true as all recommendations change with age. Do the authors mean the cut-off for starting treatment?

    The current standard of care is to keep PHE levels below 360 for all ages. This is the principle behind the "treatment for life" standard in PKU. The study results support this standard of care.

Paragraph 3: Meta-analytic Methods:
Explain the terms (hierarchical, fixed and random effects, un-normalized, non-informative, Pr, theta,y) and the equation also in terms of the study. I am not sure whether the average reader of the article (and I hope there will be many) will understand conditional probabilities the symbol for proportionality and the Bayesian ruse of estimating the posterior probabilities from the prior known information.

    theta,y,pr are already defined in the text. However, the following changes were implemented to address these concerns:
    - added conditional symbol definition on page 4
    - added an explanation of fixed and random effects on page 4
    - added defintion of non-informative prior on page 4
    - un-normalized has been removed from the text
    - added an explanation of hierarchical on page 4-5

Page 4, line 41: The statement "we view them (the studies included in the meta-analysis) as exchangeable samples from a population of possible PKU studies." does not fit the discussion of a possible selection of studies included into the meta-analysis.

    Exchangeable neither implies random nor independent, so its not clear how our selection of studies would influence this assumption. Exchangeability is a relatively weak assumption in general, but is one of the justifications for using hierarchical models.

Page 5, line 27: Explain more details of the equation; what is the term "o"

    Subscripts are now fully described in the subsequent sentence.

Page 5, line 42: Excluding the numerical age variable from the analysis might be reasonable for the present model. However, regarding the first years of life this is against all evidence. In addition we could not find any sound definition what the authors mean by younger and older. The age of 6 years might have been a cut-off, but this is not at all clear in table 1. Last not least a dichotomous age variable will not fit basic biological and psychological theories of development.

    We did attempt to fit models with age as a direct covariate, but these models did not perform well. Based on goodness of fit metrics, the critical period dichotomization appears to be adequate for characterizing important age differences for the purposes of this model. We do not claim our work to be any sort of comprehensive mechanistic biological model -- it is a simple PHEnomenological model, but sometimes simple models are adequate for prediction.

Page 5, line 51: Explain the equation, including the difference between "?" and "?". It would be helpful to learn earlier that TAU=1/VAR.

    The explanation of this equation has been added. We have also restated the model in terms of variance, rather than precision (inverse variance), since using precision is just a technical convenience that will likely just confuse readers.

Page 6, line 13: The reader might feel stimulated to put y=IQ into the equation on page 4. Is this really appropriate?

    We assume the reviewer means the equation on page 6 (?). For clarity, we have actually done this substitution, since they do correspond, so there is no need for an extra variable defintion.

Page 6, line 24: explain the equation and its terms (n, r, and ?). 

    We have added a description for n. The other terms were described. this paragraph is mainly for the beneifit of either technical readers, or for someone trying to replicate the analysis. It is not critical for the clinical reader.

Is rj on line 26 a typo?

    No, ri in the equation was a typo. This has been corrected.

Page 6, line 40: After all these equations a switch to Figure 2 will not be easy for the average reader.

    We have tried to clarify the figure as much as possible. We believe that some readers will be aided either by the figure or by the description in the methods, but perhaps not both. We hope that between them, however, the essence of the model will be communicated.

Do the studies included into the analysis really cover a PHE range up to 3000µM (50mg/dl)?

    They do not. in figure 3, we have shaded grey the region of the model that predicts beyond the range of the data from the studies, so that the reader can be aware of extrapolation.

Page 7, Paragraph 4 Results:

It would be helpful for the reader if parameters could be directly identified in Table 2 and could be traced back to the equations explained in paragraph 3.

    We have edited the caption for the table to refer to the parameters of the equations.

The authors should be more explicit in using effects and BCIs. The positive concurrent PHE effect should either be explained (probably not easy) or sacrificed as statistically not proven. All effects should be interpreted with reference to BCIs (also those including zeros).

    The parameter estimates of the model are discussed along with the credible intervals in the 5th paragrath of the results. There are no associated credible intervals for the predicted probabilities because they are integrated tail probabilities. They essentially integrate over the posterior uncertainty of the model. We are not sure about what the reviewer is referring to in "the positive concurrent PHE effect" because both PHE effects are nominally negative. The only positive value is the critical period effect in the concurrent model, and this estimate has a wide credible interval that includes reasonable probability of being negative. Note that we are not doing statistical hypothesis testing here; we are using the model for estimation.

Page 7, lines 13-18: Is it justified to model the Phe scale up to 3000 µmol/L regarding the PHE levels measured in the studies included into the meta-analysis?

    We have amended the figure to show where the model is extrapolating beyond the data. We prefer this to truncating the model because some may be interested in what the model predicts.

Page 8, line 40: Why do the authors use 500 µmol/l as a result and switch to 400 and 360 µmol/L in the discussion (page 9, line28)? 

    500 was just a convenient reference point; we have changed it to 400 to be consistent.

Please notice that at 250 µM the model predicts a value (0.1) that is lower (!) than the general population value.

    This is not surprising, given that this is at the lower extreme of a parametric model. We could have fixed this endpoint to the population values, but chose to let the data provide all the evidence for the analysis. We are not as concerned about the prediction at this end of the range, particularly.

Page 8, line 42: If the sentence "The probabilities corresponding to historical measures of blood Phe (top two dark lines in Figure 3) demonstrate an increasing chance of low IQ with increasing Phe," is true, one could come to the conclusions that at a Phe level of 1250 µmol/L the probability to have an IQ in the normal range would be 0.25 and 50% of patients with levels of about 900 µmol/l will be in the normal band. Would this mean that many patients are overtreated?

    Please note that this model describes the relationship between PHE and IQ for *treated* cases. Aside from this, reading from figure 3, the probability of a normal IQ (>85) in the worst case (critical, historical) is approximately 35% (i.e. 1-0.35), not zero.

Page 9, lines 2-4: Using concurrent PHE levels predicting IQs dichotomized at cut-off levels would imply that changing concurrent PHE levels will result in IQs changes and therefore reversibility of the PHE effect. This result needs discussion.

    We have added a sentence at the end of the fourth paragraph of the discussion that clarifies this.

Discussion:
The discussion is largely a repetition of the results paragraph.
There are four statements needing more explanation.

First, it is stated that PHE effects are leveling off at 2000 µmol/L, although data in the original studies do not cover this range of values. The statement might be based on mathematical extrapolation but not on data.

    This is extrapolation, and we have amended the figure and text to reflect where the model predicts beyond the data.

Second, the effect of historical PHE levels outside the critical period refer to a single age range beyond 6 years and thereby might merge the periods of childhood, adolescence and early adulthood, not necessarily justifying the statement that "the need for dietary control continues throughout the lifetime." (page 9, lines 42-43).

    We have modified this sentence for clarity, however we disagree with the reviewer if the suggestion is that there is an age at which an individual with pku should not be treated. The current standard of care is lifetime treatment, and our results provide support for this standard.

Third, the statement, that "adverse effects take time to manifest" provokes an explanation how this could manifest in the CNS.

    Our paper deals only with effects on IQ. we have clarified this by changing "adverse effects ..." to "reduction in IQ".

Fourth, cognitive outcome (page 10, line 2) is more than IQ. There is a sound base of evidence, that concurrent PHE levels can have effects on more specific variables like information processing and reaction time.

    We wholeheartedly agree with the reviewer on this point, but early in the systematic review process, we concluded that there were not sufficient data to tackle other response variables, so we chose to focus exclusively on IQ.

Page 10, line 23: alpha0 and alpha 1 are not represented in figure 2

    We have amended these to refer to the labels actually used in the figure.

Minor concerns:

page 2, lines 22-27: As also patients with classical PKU have (PAH deficient) hyperPHEnylalaninemia the more appropriate term for hyperPHEnylalaninemia would be Mild HyperPHEnylalnineamia (MHP). 1000 µmol/L is no more a good threshold for MPH.

    The definitions used in this paper are based on the published pku literature and were confirmed with stakeholders and experts in the field during our systematic review. The specific terms suggested for an elevated PHE level that is above or below 1000 are not endorsed by the larger PKU community. More importantly, the specific terms that are used are not essential to the results or implications of this paper, as any level above 360 should be treated regardless of the term that is used.

Page 2, line 28: If it would be known what safe means, this would be true, but it isn't. Maybe "low" would be a better term?

    This suggestion has been implemented.

Page 4, line 7: What do the authors mean by retrospective cohort studies? In the strict definition these would be case-control studies with a relatively week experimental power.

    We refer to these studies as retrospective cohort studies because cases are identified by intervention, not by outcome.

Page 5, line 4: what is meant by ".. a notional population parameters."?

    We have clarified this in the text.


Tables and Figures:

Table 1
Sample sizes might be misleading
e.g. Anastasoaie et al. (2008) report IQ tests for 32 and DQ tests for 28 children. However, it is not obvious whether data were available for all 46 subjects included in the study (see tables 1 and 2)
It is not clear how data have been selected for different periods
e.g. Anastasoaie (2008) report data for three periods (0-6, 0-10, >10 yrs)
with a toral age range 2.9-15.5. The study is labled as critical in Table 1

    The extracted data and results came from the abstract, not the table, because this was the only place that all the required components (including correlation coefficients) were presented together. There, it indicates that the sample size is 46. In any case, it has little impact on our results, since n is not used in any of our calculations. It only factors in indirectly, via the correlation coefficient and associated p-value.

Weglage 2001: Type of Phe Measurement is labelled historical critical. Historical Phe levels are computed for periods 0-10 and >10. Concurrent Phe levels are not included in the meta-analysis.

    We used historical measurements, during both the critical and non-critical periods. Table 1 has been amended to reflect this.

Weglage (1995) is not included in the reference list.

    This was wrongly labelled in the table; it should have been Weglage 1999.

Do the authors have checked multiple report of data in the three publications by Weglage? All these data come from a single centre. Nine of the 15 patients reported in Weglage (2001) fall in the age range of the Weglage (2000) publication.

    We extracted PHE measurements from <10 year old patients only from weglage 2001 and 10-18 years from Weglage 2000. 

Table 2: Explain E(IQ). Is SD the right dispersion parameter for the Median?

    Yes, the sd is the standard deviation of the posterior distribution of the parameter, which corresponds to a standard error in frequentist terms.

Figure 1: Explain why age ranges of historical critical and non-critical are opverlapping

    The figure just shows arbitrary examples for each scenario, for illustration. They are both historical becuase of the difference between the PHE and IQ measurement, and one is critical because the Phe measurement took place in the critical period. There is no reason they should not overlap.

Figure 2: Explain the term "RE". The reader will search for the non-critical period as well as for concurrent PHE.

    Definition has been added to the caption. We also added data nodes for PHE and critical period to aid interpretation.

Figure 3: If the PHE variable is modelled in steps of 200 µmol/L and 400 µmol/l is an important result, I would expect the x-axis of figure 3 scaled accordingly.

    The scale has been adjusted.

Figure legend: there are no triangles in figure 3

    The figure caption has been corrected.

General concerns
The authors should discuss the interpretation of the IQ data of the different studies included in their analysis. Have the original studies controls groups included. What about other confounding variables like socio-economic status? Have different IQ tests been used?

    We have included the IQ measurement instrument in table 1. There were a variety of methods used, sometimes even within studies. one study did not even report which method was used. The stakeholders and experts consulted during the systematic review did not express concern regarding this source of variation. We have added discussion of this in the methods.

What is the primary goal of the study? Methodology, results, or both?

    The goal of the study was to quantitatively summarize the evidence for a PHE-IQ relationship. The methodological innovation was a by-product of this goal, but may be of equal value to the scientific community.

Results should be discussed together with those of other types of research, in particular those published in the contest of large longitudinal studies (USCSPKU, German CSPKU, British PKU register).

    The published literature from these groups was already considered and reviewed in the process of doing the systematic review that led to this article. Those groups may respond to the data in the paper once it is published.

Historical and concurrent Phe levels often are correlated. What is the implication for the results?

    This correlation is accounted for in the random effects. All measurements from the same study share a random effect value, so they will be correlated in the model.


Reviewer #3: The premise of the article and the analytic approach are excellent. The paper is very well written. I have only a few suggestions(noted below).

I believe the authors should include some additional comments in the Introduction and Discussion regarding the fact that IQ is a general/summary indicator of cognitive ability that fails to capture specific difficulties in cognition experienced by individuals with PKU. The authors should remind readers that IQ is a composite of many cognitive abilities rather than an indicator of ability in important, specific domains (e.g., executive, long-term episodic memory, etc.). As stated in the abstract, the relationship between Phe levels and IQ is easily interpreted by clinicians. It is important to remember, however, that potentially valuable information should not be ignored for the sake of ease (i.e., only examining IQ).

    The discussion has been amended to draw attention to these points.

I would also like to see the authors make additional recommendations for future studies. For example, should large scale studies be conducted to examine relationships between Phe levels and specific domains of cognition (following comments in the previous paragraph)? What do the authors see as next steps?

    A paragraph on future research has been added to the discussion (final paragraph).

In the Discussion the authors state: "By combining information from several studies that measured both Phe and IQ in individuals with PKU, we characterized the extant evidence of the relationship between specific blood Phe levels and IQ, the impact of the critical period on cognition and the best timing for Phe and IQ measurement in order to determine these effects." The authors are to be applauded for this nice piece of work. That said, is it possible to take the results further? For example, is it possible to do something like identify inflection points on the regression lines (I apologize for my lack of statistical expertise here) that indicate Phe levels before which IQ begins to decline??

    In this work, we have only fit linear models, due mainly to the lack of information for fitting higher-order models. Hence, there is no inflection point. The only viable alternative to what we have done, given the information at hand, would have been some sort of nonparametric approach.

Finally, I do not believe Figure 1 adds much to the paper beyond information which either is already or could be included in the text.

    We have found this figure to be useful in oral presentations for explaining the four different scenarios described by the model, therefore we would prefer to retain it in the manuscript.