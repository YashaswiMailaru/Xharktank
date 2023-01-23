from rest_framework import serializers

from .models import Pitch, CounterOffer

class PitchSerializer(serializers.ModelSerializer):
    entrepreneur = serializers.CharField(max_length=120)
    pitchTitle = serializers.CharField(max_length=120)
    pitchIdea = serializers.CharField(max_length=300)
    askAmount = serializers.FloatField()
    equity = serializers.FloatField()
    class Meta:
        model = Pitch
        fields = ('entrepreneur', 'pitchTitle', 'pitchIdea', 'askAmount', 'equity', 'id', 'offers')
    def create(self, validated_data):
        pid = Pitch.objects.create(**validated_data)
        return pid

    def update(self, instance, validated_data):
        instance.entrepreneur = validated_data.get('entrepreneur', instance.entrepreneur)
        instance.pitchTitle = validated_data.get('pitchTitle', instance.pitchTitle)
        instance.pitchIdea = validated_data.get('pitchIdea', instance.pitchIdea)
        instance.askAmount = validated_data.get('askAmount', instance.askAmount)
        instance.equity = validated_data.get('equity', instance.equity)
        instance.save()
        return instance

class CounterOfferSerializer(serializers.ModelSerializer):
    investor = serializers.CharField(max_length=120)
    comment = serializers.CharField(max_length=300)
    amount = serializers.FloatField()
    equity = serializers.FloatField()
    class Meta:
        model = CounterOffer
        fields = ('investor', 'comment', 'amount', 'equity')
    def create(self, validated_data):
        cid = CounterOffer.objects.create(**validated_data)
        return cid

    def update(self, instance, validated_data):
        instance.entrepreneur = validated_data.get('investor', instance.investor)
        instance.pitchTitle = validated_data.get('comment', instance.comment)
        instance.pitchIdea = validated_data.get('amount', instance.amount)
        instance.equity = validated_data.get('equity', instance.equity)
        instance.save()
        return instance