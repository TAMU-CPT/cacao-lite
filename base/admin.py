from django.contrib import admin
from .models import GAF, Challenge, Assessment, Paper, Gene, Organism, RefSeq

class GAFAdmin(admin.ModelAdmin):
    list_display = ('id', 'gene', 'owner', 'db', 'qualifier', 'review_state', 'go_id', 'db_reference', 'date')

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('id', 'challenge_gaf', 'original_gaf', 'date')

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'gaf', 'challenge', 'date')

class PaperAdmin(admin.ModelAdmin):
    list_display = ('pmid', 'pub_year', 'title', 'pmc')

class GeneAdmin(admin.ModelAdmin):
    list_display = ('id', 'start', 'end', 'strand', 'refseq')

class OrganismAdmin(admin.ModelAdmin):
    list_display = ('id', 'common_name', 'taxon', 'ebi_id')

class RefSeqAdmin(admin.ModelAdmin):
    list_display = ('id', 'organism')

admin.site.register(GAF, GAFAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(Paper, PaperAdmin)
admin.site.register(Gene, GeneAdmin)
admin.site.register(Organism, OrganismAdmin)
admin.site.register(RefSeq, RefSeqAdmin)
