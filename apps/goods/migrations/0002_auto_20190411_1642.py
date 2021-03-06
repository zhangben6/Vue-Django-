# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-11 08:42
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner', verbose_name='轮播图片')),
                ('index', models.IntegerField(default=0, verbose_name='轮播顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '首页轮播',
                'verbose_name_plural': '首页轮播',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商品轮播',
                'verbose_name_plural': '商品轮播',
            },
        ),
        migrations.CreateModel(
            name='HotSearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(default='', max_length=20, verbose_name='热搜词')),
                ('index', models.IntegerField(default=0, verbose_name='排序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '热搜排行',
                'verbose_name_plural': '热搜排行',
            },
        ),
        migrations.CreateModel(
            name='IndexAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '首页广告',
                'verbose_name_plural': '首页广告',
            },
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '商品信息', 'verbose_name_plural': '商品信息'},
        ),
        migrations.AlterModelOptions(
            name='goodscategorybrand',
            options={'verbose_name': '宣传品牌', 'verbose_name_plural': '宣传品牌'},
        ),
        migrations.AddField(
            model_name='goods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AddField(
            model_name='goods',
            name='click_num',
            field=models.IntegerField(default=0, verbose_name='点击数'),
        ),
        migrations.AddField(
            model_name='goods',
            name='fav_num',
            field=models.IntegerField(default=0, verbose_name='收藏数'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_brief',
            field=models.TextField(default='', max_length=500, verbose_name='商品简短描述'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_desc',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='内容'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_front_image',
            field=models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='封面图'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_num',
            field=models.IntegerField(default=0, verbose_name='库存数'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_sn',
            field=models.CharField(default='', max_length=50, verbose_name='商品唯一货号'),
        ),
        migrations.AddField(
            model_name='goods',
            name='is_hot',
            field=models.BooleanField(default=False, help_text='是否热销', verbose_name='是否热销'),
        ),
        migrations.AddField(
            model_name='goods',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='是否新品'),
        ),
        migrations.AddField(
            model_name='goods',
            name='market_price',
            field=models.FloatField(default=0, verbose_name='市场价格'),
        ),
        migrations.AddField(
            model_name='goods',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='商品名'),
        ),
        migrations.AddField(
            model_name='goods',
            name='ship_free',
            field=models.BooleanField(default=True, verbose_name='是否承担运费'),
        ),
        migrations.AddField(
            model_name='goods',
            name='shop_price',
            field=models.FloatField(default=0, verbose_name='本店价格'),
        ),
        migrations.AddField(
            model_name='goods',
            name='sold_num',
            field=models.IntegerField(default=0, verbose_name='商品销售量'),
        ),
        migrations.AddField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='goods.GoodsCategory', verbose_name='父类目级别'),
        ),
        migrations.AddField(
            model_name='indexad',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AddField(
            model_name='indexad',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.Goods'),
        ),
        migrations.AddField(
            model_name='goodsimage',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='banner',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品'),
        ),
    ]
